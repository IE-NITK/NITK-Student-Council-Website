from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from profiles.forms import ProfileForm
from .models import *
from braces.views import LoginRequiredMixin

# Create your views here.

def indexPage(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        password = request.POST.get('password','')
        user = auth.authenticate(email=username,password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/smriti/home/')
        else:
            return HttpResponseRedirect('/smriti/invalid/')
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect('/smriti/home/')
        return render(request,'smriti/index.html')

@login_required
def homePage(request):
    testimonials = Testimonial.objects.filter(testimonial_to=request.user)
    profile = Profile.objects.get(user=request.user)
    return render(request,"smriti/home.html",{'testimonials':testimonials,'profile':profile})

def browsePage(request):
    final_years = Profile.objects.filter(rollno__contains="12")
    ch = final_years.filter(branch='CH')
    co = final_years.filter(branch='CO')
    cv = final_years.filter(branch='CV')
    ec = final_years.filter(branch='EC')
    ee = final_years.filter(branch='EE')
    it = final_years.filter(branch='IT')
    me = final_years.filter(branch='ME')
    mn = final_years.filter(branch='MN')
    mt = final_years.filter(branch='MT')
    return render(request,"smriti/browse.html",{'ch':ch,
                                                'co':co,
                                                'cv':cv,
                                                'ec':ec,
                                                'ee':ee,
                                                'it':it,
                                                'me':me,
                                                'mn':mn,
                                                'mt':mt,
                                                })

def searchPage(request):
    if request.method == 'POST':
        search_param = request.POST.get('search_param','')
        final_years = Profile.objects.filter(rollno__contains="12")
        name_result = final_years.filter(user__name__icontains=search_param)
        roll_result = final_years.filter(rollno__icontains=search_param)
        results = name_result | roll_result
        return render(request,"smriti/search.html",{'results':results, 'key':search_param})
    if request.method == 'GET':
        return render(request,'smriti/search.html')

def testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    return render(request, "smriti/testimonial.html", {'testimonial':testimonial})

class WritePage(generic.TemplateView):
    template_name = "smriti/write.html"

def profilePage(request, rollno):
    profile = get_object_or_404(Profile, rollno__iexact=rollno)
    testimonials = Testimonial.objects.filter(testimonial_to=profile.user)
    return render(request,"smriti/home.html",{'testimonials':testimonials,'profile':profile})

@login_required
def writeTestimonial(request, rollno):
    testimonial_to = get_object_or_404(Profile, rollno__iexact=rollno)
    if request.method == "GET":
        testimonial = Testimonial.objects.filter(testimonial_to=testimonial_to.user, created_by=request.user)
        if testimonial.exists():
            current_content = testimonial[0]
            return render(request,"smriti/write.html", {'to':testimonial_to, "testimonial" : current_content})
        else:
            return render(request,"smriti/write.html", {'to':testimonial_to})
    elif request.method == "POST":
        content = request.POST.get('content','')
        test, created = Testimonial.objects.get_or_create(
            testimonial_to=testimonial_to.user,
            created_by = request.user,
        )
        test.description = content.strip()
        test.save()
        return redirect("/smriti/profiles/"+testimonial_to.rollno)

class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "smriti/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_form = ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            profile_form = ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                profile_form=profile_form)
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Profile details saved!")
        return redirect("smriti:home")

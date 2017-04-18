from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.conf import settings
from profiles.models import Profile
from profiles.forms import ProfileForm
from .models import *
from .mails import sendgrid_mail
from braces.views import LoginRequiredMixin
import django_rq
# Create your views here.

def sort_by_rollno(queryset):
    return sorted(queryset, key=lambda x:int(x.rollno[4:]))

def indexPage(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        password = request.POST.get('password','')
        user = auth.authenticate(email=username,password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/smriti/home/')
        else:
            return render(request,'smriti/index.html', {"errors":"Invalid Login Credentials. Please try again with correct credentials."})
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
    cornercase = Profile.objects.filter(rollno="11IT26")
    ch = sort_by_rollno(final_years.filter(branch='CH'))
    co = sort_by_rollno(final_years.filter(branch='CO'))
    cv = sort_by_rollno(final_years.filter(branch='CV'))
    ec = sort_by_rollno(final_years.filter(branch='EC'))
    ee = sort_by_rollno(final_years.filter(branch='EE'))
    it = sort_by_rollno(final_years.filter(branch='IT'))
    me = sort_by_rollno(final_years.filter(branch='ME'))
    mn = sort_by_rollno(final_years.filter(branch='MN'))
    mt = sort_by_rollno(final_years.filter(branch='MT'))
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

def send_new_testimonial_mail(to, writer, id):
    subject = "New testimonial on Smriti from "+ writer.name
    link = "http://students.nitk.ac.in"+reverse("smriti:testimonial", args=[id])
    content = "Hello "+ to.name + """,
    <br><br> You have a new testimonial on Smriti from """+ writer.name +""".

    <br><br>You can view it at """+ link + """.<br><br>

    Regards,<br>
    Smriti 2016 Team, IE-NITK
    <br><br>
    <%asm_group_unsubscribe_url%>
    """

    asm_group = settings.SENDGRID_TESTIMONIAL_ASM_ID
    sendgrid_mail(to.email, subject, content, asm_group)

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
        if content.strip() == "":
            return render(request, "smriti/generic.html", {"content":"Sorry! Blank testimonials are not allowed."})
        test, created = Testimonial.objects.get_or_create(
            testimonial_to=testimonial_to.user,
            created_by = request.user,
        )
        test.description = content.strip()
        test.save()
        if created:
            django_rq.enqueue(send_new_testimonial_mail, testimonial_to.user, request.user, test.id)
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

def feed(request):
    testimonial_list = Testimonial.objects.all()
    paginator = Paginator(testimonial_list, 50)
    page = request.GET.get('page')
    try:
        testimonials = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        testimonials = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        testimonials = paginator.page(paginator.num_pages)
    return render(request, "smriti/feed.html", {"testimonials": testimonials})

@login_required
def deleteTestimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if not (request.user == testimonial.testimonial_to or request.user == testimonial.created_by):
        return render(request, "smriti/generic.html", {"content":"You dont have permissions."})
    testimonial.delete()
    return render(request, "smriti/generic.html", {"content":"Your testimonial has been deleted."})

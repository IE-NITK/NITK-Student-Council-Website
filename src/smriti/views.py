from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from .models import *

# Create your views here.

def indexPage(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        password = request.POST.get('password','')
        user = auth.authenticate(email=username,password=password)
        if user is not None:
            return HttpResponseRedirect('/smriti/home/')
        else:
            return HttpResponseRedirect('/smriti/invalid/')
    if request.method == 'GET':
        return render(request,'smriti/index.html')

@login_required
def homePage(request):
    testimonials = Testimonial.objects.filter(testimonial_to=request.user)
    profile = Profile.objects.get(user=request.user)
    return render(request,"smriti/home.html",{'testimonials':testimonials,'profile':profile})

def browsePage(request):
    ch = Profile.objects.filter(branch='CH')
    co = Profile.objects.filter(branch='CO')
    cv = Profile.objects.filter(branch='CV')
    ec = Profile.objects.filter(branch='EC')
    ee = Profile.objects.filter(branch='EE')
    it = Profile.objects.filter(branch='IT')
    me = Profile.objects.filter(branch='ME')
    mn = Profile.objects.filter(branch='MN')
    mt = Profile.objects.filter(branch='MT')
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
        name_result = Profile.objects.filter(user__name__icontains=search_param)
        roll_result = Profile.objects.filter(rollno__iexact=search_param)
        return render(request,"smriti/search.html",{'name_result':name_result,'roll_result':roll_result})
    if request.method == 'GET':
        return render(request,'smriti/search.html')

class TestimonialPage(generic.TemplateView):
    template_name = "smriti/testimonial.html"

class WritePage(generic.TemplateView):
    template_name = "smriti/write.html"

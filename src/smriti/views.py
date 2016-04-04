from django.shortcuts import render
from django.views import generic
from django.contrib import auth
from django.http import HttpResponseRedirect

# Create your views here.
class IndexPage(generic.TemplateView):
    template_name = "smriti/index.html"

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        password = request.POST.get('password','')
        user = auth.authenticate(email=username,password=password)

        if user is not None:
            return HttpResponseRedirect('/smriti/home/')
        else:
            return HttpResponseRedirect('/smriti/invalid/')

class HomePage(generic.TemplateView):
    template_name = "smriti/home.html"

from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexPage(generic.TemplateView):
    template_name = "smriti/index.html"

class HomePage(generic.TemplateView):
    template_name = "smriti/home.html"

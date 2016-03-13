from django.shortcuts import render
from .models import *
from django.views import generic
from django.core import serializers
import json
# Create your views here.

class represent(generic.TemplateView):
    template_name = "represent.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class MessagePage(generic.TemplateView):
	template_name = "message.html"

class ClubLifePage(generic.TemplateView):
	template_name="clublife.html"

class ContactNumbers(generic.TemplateView):
	template_name="contacts.html"

class NewsPage(generic.TemplateView):
	template_name="news.html"

def date_handler(obj):
    # To handle the date format while JSON conversion
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def calEvents(request):
    objectQuerySet = Events.objects.values('id','title','start','end')
    events = json.dumps(list(objectQuerySet), default=date_handler)
    return render(request, 'calendar.html', {'eventlist':events})

def homePage(request):
    eventlist = Events.objects.all().order_by('-start')[:5]
    newslist = News.objects.all().order_by('-timestamp')[:5]
    articlelist = Articles.objects.all().order_by('-published')[:5]
    return render(request,'home.html',{'events':eventlist,'news':newslist,'articles':articlelist})

def announcements(request):
    announcelist = Announcements.objects.all().order_by('timestamp')
    return render(request,'announce.html',{'announcements':announcelist})

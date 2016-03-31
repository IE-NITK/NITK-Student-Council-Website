from django.shortcuts import render
from .models import *
from django.views import generic
from django.core import serializers
import json
# Create your views here.

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class MessagePage(generic.TemplateView):
	template_name = "message.html"

class Blog(generic.TemplateView):
	template_name = "blog.html"

class ContactNumbers(generic.TemplateView):
	template_name="contacts.html"

class NitkLifePage(generic.TemplateView):
    template_name = "nitk_life.html"

class SenatePage(generic.TemplateView):
    template_name = "senate.html"

class FAQ(generic.TemplateView):
    template_name="faq.html"

class Resources(generic.TemplateView):
    template_name = "resources.html"

def date_handler(obj):
    # To handle the date format while JSON conversion
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def calEvents(request):
    objectQuerySet = Events.objects.values('id','title','start','end')
    events = json.dumps(list(objectQuerySet), default=date_handler)
    return render(request, 'calendar.html', {'eventlist':events})

def homePage(request):
    eventlist = Events.objects.all().order_by('-start')[:3]
    newslist = News.objects.all().order_by('-timestamp')[:3]
    articlelist = Articles.objects.all().order_by('-published')[:3]
    return render(request,'home.html',{'events':eventlist,'news':newslist,'articles':articlelist})

def announcements(request):
    announcelist = Announcements.objects.all().order_by('-timestamp')
    return render(request,'announce.html',{'announcements':announcelist})

def blogPage(request, num=0):
    if num:
        article = Articles.objects.get(id=num)
        return render(request,'article.html',{'article':article})
    else:
        articles = Articles.objects.all().order_by('-published')
        return render(request,'blog.html',{'article':articles})

def newsPage(request, num=0):
    if num:
        news = News.objects.get(id=num)
        return render(request,'eachNews.html',{'news':news})
    else:
        news = News.objects.all().order_by('-timestamp')
        inthenews = news.filter(category='N')
        spotlight = news.filter(category='S')
        campus = news.filter(category='C')
        pinned = news.filter(pinned=True)
        return render(request,'news.html',{'inthenews':inthenews,'spotlight':spotlight,'campus':campus,'pinned':pinned})

def meetTheReps(request):
    presi = Member.objects.get(designation='PR')
    inci = Member.objects.get(designation='IC')
    engi = Member.objects.get(designation='EC')
    sec = Member.objects.get(designation='GS')
    grep = Member.objects.get(designation='GR')
    pgrep = Member.objects.get(designation='PG')
    first = Member.objects.filter(year=1).filter(designation='CR')
    second = Member.objects.filter(year=2).filter(designation='CR')
    third = Member.objects.filter(year=3).filter(designation='CR')
    final = Member.objects.filter(year=4).filter(designation='CR')
    return render(request,'represent.html',{'presi':presi,'inci':inci,'engi':engi,'sec':sec,'grep':grep,'pgrep':pgrep,'first':first,'second':second,'third':third,'final':final})

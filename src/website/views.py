from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import  EventsForm
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core import serializers
from django.core.mail import send_mail
import json
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class AboutPage(generic.TemplateView):
    template_name = "about.html"

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

def announcement(request, id):
    announcement = get_object_or_404(Announcements, id=id)
    return render(request,'announce_ind.html',{'announcement':announcement})

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

def minutes(request):
    minuteslist = Minute.objects.all().order_by('-date_of_meeting')
    return render(request, 'minutes.html', {'minutes':minuteslist})

def mous(request):
    mouslist = MoU.objects.all().order_by('-date_of_signing')
    return render(request, 'mous.html', {'mous':mouslist})

def grants(request):
    grantlist = ResearchGrant.objects.all().order_by('-date_of_grant')
    return render(request, 'grants.html', {'grants':grantlist})

def resources(request):
    categories = ResourceCategory.objects.all().order_by("name")
    resourcelist = Resource.objects.all().order_by('-timestamp')
    reports = {}
    for category in categories:
        reports[category.name] = resourcelist.filter(category=category)
    return render(request, 'resources.html', {'resources':reports})

def reports(request):
    reportlist = SenateReport.objects.all().order_by('-date_of_report')
    return render(request, 'senatereports.html', {'reports':reportlist})

def meetTheReps(request):
    presi = CoreMember.objects.get(designation='PR')
    vpresi = CoreMember.objects.get(designation='VP')
    sec = CoreMember.objects.get(designation='GS')
    jsecu = CoreMember.objects.get(designation='JU')
    jsecp = CoreMember.objects.get(designation='JP')
    pggrep = CoreMember.objects.get(designation='GR')
    techu = CoreMember.objects.get(designation='TU')
    techp = CoreMember.objects.get(designation='TP')
    cultu = CoreMember.objects.get(designation='CU')
    cultp = CoreMember.objects.get(designation='CP')
    inci = CoreMember.objects.get(designation='IC')
    engi = CoreMember.objects.get(designation='EC')
    engit = CoreMember.objects.get(designation='ET')
    incit = CoreMember.objects.get(designation='IT')
    engij = CoreMember.objects.get(designation='EJ')
    incij = CoreMember.objects.get(designation='IJ')
    first = Member.objects.filter(year=1)
    second = Member.objects.filter(year=2)
    third = Member.objects.filter(year=3)
    final = Member.objects.filter(year=4)
    pg = Member.objects.filter(year=5)
    phd = Member.objects.filter(year=6)
    return render(request,'represent.html',{'presi':presi,
                                            'vpresi':vpresi,
                                            'sec':sec,
                                            'jsecu':jsecu,
                                            'jsecp':jsecp,
                                            'pggrep':pggrep,
                                            'techu':techu,
                                            'techp':techp,
                                            'cultu':cultu,
                                            'cultp':cultp,
                                            'inci':inci,
                                            'engi':engi,
                                            'engit':engit,
                                            'incit':incit,
                                            'engij':engij,
                                            'incij':incij,
                                            'first':first,
                                            'second':second,
                                            'third':third,
                                            'final':final,
                                            'pg':pg,
                                            'phd':phd,
                                            })

def letters(request):
    director = Letter.objects.filter(addressee="DR").order_by("-date_of_letter")
    sw = Letter.objects.filter(addressee="SW").order_by("-date_of_letter")
    fw = Letter.objects.filter(addressee="FW").order_by("-date_of_letter")
    pnd = Letter.objects.filter(addressee="PD").order_by("-date_of_letter")
    hs = Letter.objects.filter(addressee="HS").order_by("-date_of_letter")
    mc = Letter.objects.filter(addressee="MC").order_by("-date_of_letter")
    return render(request, 'letters.html', {
        "director": director,
        "sw": sw,
        "fw": fw,
        "pd": pnd,
        "hostel": hs,
        "mc": mc
    })

def suggest(request):
    if request.method == 'GET':
        return render(request, 'suggest.html')
    if request.method == 'POST':
        name = request.POST.get('name','')
        contact = request.POST.get('contact','')
        email = request.POST.get('email','')
        content = request.POST.get('content','')
        suggestion = "From : %s \nContact Number: %s \nEmail: %s \nSuggestion: " % (name,contact,email)
        suggestion = suggestion + content
        try:
            send_mail('Suggestion', suggestion, settings.EMAIL_HOST_USER, ['studentscouncil@nitk.edu.in'], fail_silently=False)
            success = 1
            return render(request,'suggestresponse.html',{'success':success})
        except:
            success = 0
            return render(request,'suggestresponse.html',{'success':success})

def messagePage(request):
    messages = MessageFromPresident.objects.all().order_by('-year')
    return render(request,'message.html',{'messages':messages})

class ClubView(generic.ListView):
    template_name='clubs.html'
    context_object_name = 'all_clubs'

    def get_queryset(self):
        return Club.objects.all()

class ClubEventView(generic.DetailView):
    model = Club
    template_name ='club-events.html'



@login_required(login_url='/login/')
def clubEventEditView(request,pk):
    club=get_object_or_404(Club,pk=pk)
    if request.user.email != club.user.email:
        logout(request)
        return render(request,'club-events.html',{'club':club, 'error_login':'Sorry you dont have access to the Club.'})
    return render(request,'club-events-edit.html',{'club':club})
 

@login_required(login_url='/login/')
def addEvent(request,pk):
    club=get_object_or_404(Club,pk=pk)
    if request.user.email != club.user.email:
        # return redirect('/login/')
        logout(request)
        return render(request,'club-events.html',{'club':club, 'error_login':'Sorry you dont have access to the Club.'})
    
    form = EventsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        club_events = club.events_set.all()
        for event in club_events:
            if event.title == form.cleaned_data.get("title"):
                context = {
                    'club': club,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'create-event.html', context)
        event = form.save(commit=False)
        event.organizer = club
        event.save()
        return redirect('/clubs/'+str(club.id)+'/edit')

    context = {
        'club': club,
        'form': form,
    }
    return render(request, 'create-event.html', context)

class EditEventView(LoginRequiredMixin,UpdateView):
    model = Events
    fields = ['title','details','start','end','contact']
    login_url = '/login/'
    
    def form_valid(self,form):
        club=Club.objects.get(pk=self.kwargs['id'])
        if self.request.user.email != club.user.email:
            logout(self.request)
            return render(self.request,'club-events.html',{'club':club, 'error_login':'Sorry you dont have access to the Club.'})
        if form.is_valid():
            form.save()
            return redirect('/clubs/'+str(club.id)+'/edit')

class DeleteEventView(LoginRequiredMixin,DeleteView):
    model = Events
    login_url = '/login/'
    
    def get_success_url(self):
        id=self.kwargs['id']
        return '/clubs/'+str(id)+'/edit/'

    def get(self,request,id,pk):
        club=Club.objects.get(pk=self.kwargs['id'])
        if request.user.email == club.user.email:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            logout(self.request)
            return render(self.request,'club-events.html',{'club':club, 'error_login':'Sorry you dont have access to the Club.'})
        
    

class EventView(generic.DetailView):
    model = Events
    template_name ='events.html'
    

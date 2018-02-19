from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from django.urls import reverse_lazy
from .models import Startup,Event

class IndexView(generic.ListView):
    template_name='startups/index.html'
    context_object_name = 'all_startups'

    def get_queryset(self):
        return Startup.objects.all()

class DetailView(generic.DetailView):
	model=Startup
	template_name='startups/details.html'

class EventView(generic.DetailView):
	model=Event
	template_name='startups/events.html'
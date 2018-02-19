from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from django.urls import reverse_lazy
from .models import Club,Event

class IndexView(generic.ListView):
    template_name='clubs/index.html'
    context_object_name = 'all_clubs'

    def get_queryset(self):
        return Club.objects.all()

class DetailView(generic.DetailView):
	model=Club
	template_name='clubs/details.html'

class EventView(generic.DetailView):
	model=Event
	template_name='clubs/events.html'
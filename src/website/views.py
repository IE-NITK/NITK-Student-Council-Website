from django.shortcuts import render
from .models import *
import simplejson
from django.core.serializers import DjangoJSONEncoder
# Create your views here.

def calEvents(request):
    events = []
    for event in Events:
        events.append({'title': event.title, 'start': event.start, 'end': event.end})
    return render(request, 'calendar.html', simplejson.dumps(events, cls=DjangoJSONEncoder))

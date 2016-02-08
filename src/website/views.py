from django.shortcuts import render
from .models import Events
#from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
# Create your views here.

def calEvents(request):
    #events = []
    #eventlist = Events.objects.all()
    #for event in eventlist:
    #    events.append({'title': event.title, 'start': event.start, 'end': event.end})
    #return render(request, 'calendar.html', json.dumps(events, cls=DjangoJSONEncoder))
    objectQuerySet = Events.objects.only('title','start','end')
    events = serializers.serialize('json', list(objectQuerySet))
    return render(request, 'calendar.html', {'eventlist':events})

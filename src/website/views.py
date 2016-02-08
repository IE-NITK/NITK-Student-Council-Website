from django.shortcuts import render
from .models import Events
#from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
# Create your views here.

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def calEvents(request):
    #events = []
    #eventlist = Events.objects.all()
    #for event in eventlist:
    #    events.append({'title': event.title, 'start': event.start, 'end': event.end})
    #return render(request, 'calendar.html', json.dumps(events, cls=DjangoJSONEncoder))
    objectQuerySet = Events.objects.values('title','start','end')
    events = json.dumps(list(objectQuerySet), default=date_handler)
    return render(request, 'calendar.html', {'eventlist':events})

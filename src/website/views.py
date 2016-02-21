from django.shortcuts import render
from .models import Events
#from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
# Create your views here.

def date_handler(obj):
    # To handle the date format while JSON conversion
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def calEvents(request):
    objectQuerySet = Events.objects.values('id','title','start','end')
    events = json.dumps(list(objectQuerySet), default=date_handler)
    return render(request, 'calendar.html', {'eventlist':events})

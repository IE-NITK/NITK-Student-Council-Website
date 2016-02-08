from django.shortcuts import render
from .models import *


# Create your views here.

def calendar(request):
    return render(request, 'calendar.html', {'events': Events.objects.values('title','start','end')})

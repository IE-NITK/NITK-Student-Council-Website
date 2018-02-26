from django import forms
from django.contrib.auth.models import User

from .models import Events


class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = ['title','details','start','end','contact']

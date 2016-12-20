from _datetime import datetime
import logging

from django import forms
from django.forms.widgets import Textarea, TextInput, DateTimeInput

from DiaryWebApp.models import Entry


class EntryForm (forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # hide form labels and set required
        self.fields['title'].required = True
        self.fields['title'].label = ""
        
        self.fields['entryText'].required = True
        self.fields['entryText'].label = ""
        
        # initialise date
        self.instance.dateTime = datetime.today()
    
    def getDate(self):
        return self.instance.dateTime.today()
    
    class Meta:
        model = Entry
        fields = ('title', 'entryText' )
        widgets = {
            'title': TextInput (attrs = {'placeholder':'Entry title...'}),
            'entryText' : Textarea(attrs = {'cols': 80, 'rows': 15, 'placeholder':"What's on your mind?"}),
            'dateTime' : DateTimeInput(attrs = {'type':'dateTime'}),
        }

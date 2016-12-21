from _datetime import datetime, date
import logging

from django import forms
from django.forms.widgets import Textarea, TextInput, DateTimeInput, HiddenInput

from DiaryWebApp.models import Entry


logger = logging.getLogger(__name__)

class EntryForm (forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # hide form labels and set required
        self.fields['title'].required = True
        self.fields['title'].label = ""
        
        self.fields['entryText'].required = True
        self.fields['entryText'].label = ""
        
        self.fields['dateTime'].initial = datetime.today()

        # Assign a default date/time if creating model without saved data
        if type(self.instance.dateTime) is not datetime:
            self.instance.dateTime = datetime.today()
        
    def getDate(self):
        return self.instance.dateTime
    
    class Meta:
        model = Entry
        fields = ('title', 'entryText', 'dateTime')
        widgets = {
            'title'     : TextInput (attrs = {'placeholder':'Entry title...'}),
            'entryText' : Textarea(attrs = {'cols': 80, 'rows': 15, 'placeholder':"What's on your mind?"}),
            'dateTime'  : HiddenInput(attrs = {'type':'dateTime'}),
        }

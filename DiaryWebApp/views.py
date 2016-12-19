from django.shortcuts import render
from django.http.response import HttpResponse
import logging
import time
from DiaryWebApp.forms import EntryForm

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    text = """<h1>Welcome to version 1 of Diary Web App</h1>"""
    return HttpResponse(text)

def addEntry(request):
    entryForm = None
    template = {}
    
    if request.method == "POST":
        entryForm = EntryForm(request.POST)
        if entryForm.is_valid():
            entryForm.save(commit = True)
            return entrySubmitted(request)
        else:
            logger.info(entryForm.errors)
    else:    
        # Set up view with new entry form
        entryForm = EntryForm()
        
    date = entryForm.getDate()
    
    # Extract time and date from Entry model to populate in view
    dateAndTime = {};
    dateAndTime['entryDate'] = date.day
    dateAndTime['entryYear'] = date.year
    dateAndTime['entryDay'] = date.strftime("%A")
    dateAndTime['entryMonth'] = date.strftime("%B")
    dateAndTime['entryTime'] = date.strftime("%H:%M")
    
    # Push form and date into template vars
    template = {'form': entryForm}
    template.update(dateAndTime)
    
    logger.info("dictionary = ", template)
    
    return render(request, "DiaryEntry.html", template)

def entrySubmitted(request):
    return HttpResponse("The data was received")
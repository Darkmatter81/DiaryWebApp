import logging

from django.http.response import HttpResponse
from django.shortcuts import render, redirect,  get_object_or_404

from DiaryWebApp.forms import EntryForm
from DiaryWebApp.models import Entry
from datetime import datetime


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    text = """<h1>Welcome to version 1 of Diary Web App</h1>"""
    return HttpResponse(text)

def addEntry(request):
    entryForm = None
    
    if request.method == "POST":
        entryForm = EntryForm(request.POST)
                
        if entryForm.is_valid():
            entryForm.save(commit = True)
            return redirect('editEntry', entryForm.instance.id)
        else:
            logger.info(entryForm.errors)
    else:    
        # Set up view with new entry form
        entryForm = EntryForm()
        
    template = getEntryViewTemplate(entryForm)
    
    return render(request, "DiaryEntry.html", template)


def editEntry(request, entryId):
    # Get the latest entry from the database
    #entry = Entry.objects.get(id = entryId)
    entry = get_object_or_404(Entry, pk=entryId)
     
    if request.method == 'GET':
        entryForm = EntryForm(instance = entry)
    else:
        entryForm = EntryForm(request.POST, instance = entry)
        if entryForm.is_valid():
            entryForm.setLastUpdated(datetime.now())
            entryForm.save(commit = True)
    
    templateData = getEntryViewTemplate(entryForm)
    return render(request, "EditEntry.html", templateData)

def listEntries(request):
    return render(request, "EntriesList.html")


def getEntryViewTemplate(entryForm):
    ''' 
        Extract time and date from Entry model to populate in view
    '''
    date = entryForm.getDate()
    dateAndTime = {};
    dateAndTime['entryDate'] = date.day
    dateAndTime['entryYear'] = date.year
    dateAndTime['entryDay'] = date.strftime("%A")
    dateAndTime['entryMonth'] = date.strftime("%B")
    dateAndTime['entryTime'] = date.strftime("%H:%M")

    logger.info("time = " + dateAndTime['entryTime'])
    
    template = {'form': entryForm}
    template.update(dateAndTime)
    
    return template

def entrySubmitted(message):
    return HttpResponse(message)

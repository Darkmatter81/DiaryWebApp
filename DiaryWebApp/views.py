from django.shortcuts import render
from django.http.response import HttpResponse
import time

# Create your views here.
def index(request):
    text = """<h1>Welcome to version 1 of Diary Web App</h1>"""
    return HttpResponse(text)

def addEntry(request):
    dateAndTime = {};
    dateAndTime['entryDate'] = time.strftime("%d")
    dateAndTime['entryDay'] = time.strftime("%A")
    dateAndTime['entryMonth'] = time.strftime("%B")
    dateAndTime['entryYear'] = time.strftime("%Y")
    dateAndTime['entryTime'] = time.strftime("%H:%M")

    
    return render(request, "DiaryEntry.html", dateAndTime)
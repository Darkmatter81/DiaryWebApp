from django.contrib import admin
from DiaryWebApp.models import Entry

class EntryTableDisplay (admin.ModelAdmin):
    list_display = ('dateTime', 'lastUpdated', 'title', 'entryText')

admin.site.register(Entry, EntryTableDisplay)
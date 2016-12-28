from django.db import models


class Entry (models.Model):    
    dateTime = models.DateTimeField()
    lastUpdated = models.DateTimeField(blank = True, null = True)
    title = models.CharField(max_length = 50)
    entryText = models.CharField(max_length = 1000000)
    
    class Meta:
        db_table = 'entry'

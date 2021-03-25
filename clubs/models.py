from django.db import models
from datetime import datetime 

class Club(models.Model):
    club_name = models.CharField(max_length=200)
    club_type = models.CharField(max_length=200, default = "none")
    club_budget = models.IntegerField(default= 0)
    contactEmail = models.EmailField(default = "nullnull@null.ca")


    def __str__(self):
        return self.club_name

class Event(models.Model):
    clubname = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateTimeField('Event date', default=datetime.now)
    event_type = models.CharField(max_length=200, default = "none")
    description = models.CharField(max_length=200, default = "none")

    def __str__(self):
        return self.event_description



class Announcment(models.Model):
    clubname = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateTimeField('Event date', default=datetime.now)
    message = models.CharField(max_length=200, default = "none")

    def __str__(self):
        return self.message

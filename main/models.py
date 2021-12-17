from django.db import models
from django.db.models.fields import CharField

class ToDo(models.Model):
    text = models.CharField(default="Task", max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    persone = models.CharField(max_length=12)
    phone_number = models.IntegerField()
    date_of_meeting = models.DateField(auto_now=False)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
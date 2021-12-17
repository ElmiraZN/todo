from django.db import models
from django.db.models.fields import CharField

class ToDo(models.Model):
    text = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    persone = models.CharField(max_length=12)
    phone_number = models.PositiveIntegerField()
    date_of_meeting = models.DateField(auto_now=False)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class goal_for_month(models.Model):
    goal = models.CharField(max_length=20)
    month = models.DateField(auto_now=False)
    difficulty = models.CharField(max_length=10)
    reason_for_goal = models.TextField(max_length=200)
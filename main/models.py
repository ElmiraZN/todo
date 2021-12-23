from django.db import models
from django.db.models.fields import CharField

class ToDo(models.Model):
    text = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    person = models.CharField(max_length=12)
    phone_number = models.PositiveIntegerField()
    date_of_meeting = models.DateField(auto_now=False)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class goal_for_month(models.Model):
    goal = models.CharField(max_length=20)
    month = models.DateField(auto_now=False)
    difficulty = models.CharField(max_length=10)
    reason_for_goal = models.TextField(max_length=200)

class Habits(models.Model):
    name = models.CharField(max_length=30)
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.CharField(max_length=100)
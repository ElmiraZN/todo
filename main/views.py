from functools import partial
from typing import Text
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet, goal_for_month

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def welcome(request):
    return HttpResponse('<h1><strong>Welcome to the new page!</strong></h1>')

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, 'meeting.html', {"tomeet_list": tomeet_list})

def add_todo(request):
    form = request.POST
    text = form["todo-text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_tomeet(request):
    form = request.POST
    person = form['add-tomeet']
    # toMeet = ToMeet(person=person)
    # toMeet.save()
    print(form)
    return redirect(meeting)
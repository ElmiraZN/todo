from functools import partial
from typing import Text
from django import forms
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet, goal_for_month
from .forms import ToMeetForm

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def welcome(request):
    return HttpResponse('<h1><strong>Welcome to the new page!</strong></h1>')

def meeting(request):
    if request.method == 'POST':
        form = ToMeetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(meeting)
        else:
            return HttpResponse('The form was filled out wrong!')
    tomeet_list = ToMeet.objects.all()
    form = ToMeetForm()
    return render(request, 'meeting.html', {'tomeet_list': tomeet_list, 'form': form})

def add_todo(request):
    form = request.POST
    text = form["todo-text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

# def add_tomeet(request):
#     form = request.POST
#     # form = ToMeetForm()

#     person = form['add-tomeet_person']
#     # toMeet_p = ToMeet(person=person)
#     # toMeet_p.save()
#     print(person)

#     # form = request.POST
#     phone_number = form['add-tomeet_phone']
#     # toMeet_n = ToMeet(phone_number=phone_number)
#     # toMeet_n.save()    
#     print(phone_number)

#     # form = request.POST
#     date_of_meeting = form['add-tomeet_date']
#     # toMeet_d = ToMeet(date_of_meeting=date_of_meeting)
#     # toMeet_d.save()
#     print(date_of_meeting)
#     return redirect(meeting)
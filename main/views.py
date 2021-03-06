from functools import partial
from typing import Text
from django import forms
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from .models import Habits, ToDo, ToMeet, goal_for_month
from .forms import ToMeetForm, HabitsForm, goal_for_monthForm

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def add_todo(request):
    form = request.POST
    text = form["todo-text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

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

def delete_meeting(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(meeting)

def mark_meeting(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(meeting)

def unmark_meeting(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = False
    tomeet.save()
    return redirect(meeting)

def close_meeting(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_closed = not tomeet.is_closed
    tomeet.save()
    return redirect(meeting)

def habits(request):
    if request.method == 'POST':
        form = HabitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(habits)
        else:
            return HttpResponse('The form was filled out wrong!')
    habits_list = Habits.objects.all()
    form = HabitsForm()
    return render(request, 'habits.html', {'habits_list': habits_list, 'form': form})

def delete_habits(request, id):
    habit = Habits.objects.get(id=id)
    habit.delete()
    return redirect(habits)

def mark_habits(request, id):
    habit = Habits.objects.get(id=id)
    habit.important = True
    habit.save()
    return redirect(habits)

def unmark_habits(request, id):
    habit = Habits.objects.get(id=id)
    habit.important = False
    habit.save()
    return redirect(habits)

def close_habits(request, id):
    habit = Habits.objects.get(id=id)
    habit.done_for_today = not habit.done_for_today
    habit.save()
    return redirect(habits)

def goals(request):
    if request.method == 'POST':
        form = goal_for_monthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(goals)
        else:
            return HttpResponse('The form was filled out wrong!')
    goals_list = goal_for_month.objects.all()
    form = goal_for_monthForm()
    return render(request, 'goals.html', {'goals_list': goals_list, 'form': form})

def delete_goals(request, id):
    goal = goal_for_month.objects.get(id=id)
    goal.delete()
    return redirect(goals)

def easy_goals(request, id):
    goal = goal_for_month.objects.get(id=id)
    goal.difficulty = "easy"
    goal.save()
    return redirect(goals)

def medium_goals(request, id):
    goal = goal_for_month.objects.get(id=id)
    goal.difficulty = "medium"
    goal.save()
    return redirect(goals)

def hard_goals(request, id):
    goal = goal_for_month.objects.get(id=id)
    goal.difficulty = "hard"
    goal.save()
    return redirect(goals)

def close_goals(request, id):
    goal = goal_for_month.objects.get(id=id)
    goal.is_closed = not goal.is_closed
    goal.save()
    return redirect(goals)

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
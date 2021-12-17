from django.shortcuts import render, HttpResponse
from .models import ToDo, ToMeet, goal_for_month

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def welcome(request):
    return HttpResponse('<h1><strong>Welcome to the new page!</strong></h1>')
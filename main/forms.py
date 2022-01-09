from django.db.models import fields
from .models import ToMeet, Habits, goal_for_month
from django.forms import ModelForm, widgets, TextInput, NumberInput, DateTimeInput

class ToMeetForm(ModelForm):
    class Meta:
        model = ToMeet
        fields = ['person', 'phone_number', 'date_of_meeting']

        widgets = {
            'person': TextInput(attrs={
                'class': 'create_input',
                'placeholder': 'Name of the person',
            }),
            'phone_number': NumberInput(attrs={
                'class': 'create_input',
                'placeholder': 'Phone'
            }),
            'date_of_meeting': DateTimeInput(attrs={
                'class': 'create_input',
                'placeholder': 'Date of meeting'
            }),
        }

class HabitsForm(ModelForm):
    class Meta:
        model = Habits
        fields = ['name', 'comment']

        widgets = {
            'name': TextInput(attrs={
                'class': 'create_input',
                'placeholder': 'New habit'
            }),
            'comment': TextInput(attrs={
                'class': 'create_input',
                'placeholder': 'Comment'
            }),
        }

class goal_for_monthForm(ModelForm):
    class Meta:
        model = goal_for_month
        fields = ['goal', 'month', 'reason_for_goal']

        widgets = {
            'goal': TextInput(attrs={
                'class': 'create_input',
                'placeholder': 'Goal name',
            }),
            'month': DateTimeInput(attrs={
                'class': 'create_input',
                'placeholder': 'Execution date'
            }),
            'reason_for_goal': TextInput(attrs={
                'class': 'create_input',
                'placeholder': 'Reason for goal'
            }),
        }


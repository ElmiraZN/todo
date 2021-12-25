from django.db.models import fields
from .models import ToMeet, Habits
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
from django.db.models import fields
from .models import ToMeet
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
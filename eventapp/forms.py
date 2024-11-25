# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
# class UserRegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password1','password2']
from django import forms
from .models import Event, Participant

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_description',
            'event_location',
            'start_time',
            'end_time',
            'event_date',
            'event_organizer'
        ]
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'event_location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_organizer': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            'participant_name',
            'participant_email',
            'event_name'
        ]
        widgets = {
            'participant_name': forms.TextInput(attrs={'class': 'form-control'}),
            'participant_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'event_name': forms.Select(attrs={'class': 'form-control'}),
        }

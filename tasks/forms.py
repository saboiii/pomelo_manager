from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class CustomSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'formfield2', 'placeholder': 'Enter first name'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'formfield2', 'placeholder': 'Enter last name'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'formfield2', 'placeholder': 'Enter username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'formfield2', 'placeholder': 'Enter password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'formfield2', 'placeholder': 'Confirm password'
        })
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'formfield2',
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'formfield2',
        'placeholder': 'Enter your password'
    }))

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'progress']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'flex formfield w-1/2',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'flex formfield w-1/2',
                'placeholder': 'Enter task description',
                'rows': 4
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'block formfield w-1/2',
                'type': 'date'
            }),
            'priority': forms.Select(attrs={
                'class': 'flex formfield w-1/2'
            }),
            'progress': forms.NumberInput(attrs={
                'class': 'flex formfield w-1/2',
                'type': 'number',
                'min': '0',
                'max': '100',
                'step': '0.01'
            })
        }
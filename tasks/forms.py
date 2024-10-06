from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'progress']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'flex formfield',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'flex formfield',
                'placeholder': 'Enter task description',
                'rows': 4
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'block formfield',
                'type': 'date'
            }),
            'priority': forms.Select(attrs={
                'class': 'flex formfield'
            }),
            'progress': forms.NumberInput(attrs={
                'class': 'flex formfield',
                'type': 'number',
                'min': '0',
                'max': '100',
                'step': '0.01'
            })
        }
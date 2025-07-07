from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Task, Guest


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email', 'phone', 'img']
        widgets = {
            'img': forms.FileInput(attrs={'class': 'form-control'})
        }
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from polls.models import Post
from .models import Registration

class OrderForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Commentaire


class RegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']


class commentaireForm(UserCreationForm):
    class Meta:
        model = Commentaire
        fields = '__all__'
        exclude = ["user"]

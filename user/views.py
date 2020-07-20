from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, commentaireForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'félicitation vous être bien inscrit ' + user)
            return redirect('loginPage')
        else:
            messages.error(request, 'veuillez verifier vos information de connexion')
    datas = {
        'form':form,
    }   
    return render(request,'register.html',datas)



def loginPage(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:    
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'votre mot de passe ou email invalide')
    datas = {

    }
    return render(request, 'login.html', datas)



def deconnecte(request):
    logout(request)

    return redirect('loginPage')


def commentaire(request):
    form = commentaireForm

    if request.method =="POST":
        form = commentaireForm(request.POST)

        if form.is_valid():
            form.save()

    datas = {

    }
    return render(request, 'fashion_category.html', datas)


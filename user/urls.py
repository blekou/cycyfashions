from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('deconnecte/', views.deconnecte, name='deconnecte'),
  
]


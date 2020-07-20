from django.urls import path
from . import views

urlpatterns = [
    path('fashion/', views.fashion, name='fashion'),
    path('single/<int:pk>', views.single, name='single'),
   
]

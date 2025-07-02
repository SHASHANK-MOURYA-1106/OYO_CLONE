from django.contrib import admin
from django.urls import path
import home.views as views

urlpatterns = [
    path('', views.index, name='home'),
    
]

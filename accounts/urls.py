from django.contrib import admin
from django.urls import path
import accounts.views as views

urlpatterns = [
    path('login/' , views.login_page, name='login_page'),
    path('register/' , views.register, name='register'),
    path('verify-account/<uuid:token>/', views.verify_email_token, name="verify_email_token"),
]

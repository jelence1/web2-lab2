from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('csrf', views.csrf, name="csrf"),
    path('change_password', views.change_password, name="change_password"),
    path('csrf_yes_no', views.csrf_yes_no, name="csrf_yes_no"),
]
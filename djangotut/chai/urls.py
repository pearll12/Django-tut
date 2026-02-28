# from django.contrib import admin - no need here
from django.urls import path
from . import views #current directory import views

# localhost:8000/chai
urlpatterns = [
    path('', views.all_models, name="all-models"), #don't write / in home in python and django
]

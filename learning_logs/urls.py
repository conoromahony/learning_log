"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
# Each URL pattern is a call to the path() function, which takes three arguments.
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]

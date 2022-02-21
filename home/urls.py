from unicodedata import name
from django import views
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home_page),
    path("delete-todo/<id>/", views.delete_todo, name="delete-todo"),
    path('update-todo/', views.update_todo, name='update-todo')
]

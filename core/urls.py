from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageView.as_view(), name='home'), 
    path('home/', views.view_characters, name='home'), 
    path("create_page/", views.create_page, name="create_page"),
    path("create_character", views.create_character, name="create_character"),
]
 
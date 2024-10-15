from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.page.as_view(), name="home"),
    path("create_page", views.create_page, name="create_page"),
]

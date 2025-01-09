from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/')),  
    path('home/', views.view_characters, name='home'),  
    path('home/create_page/', views.create_page, name='create_page'),  
    path('home/create_page/create_character/', views.create_character, name='create_character'),
    path('home/chat/', views.chat, name='chat'),
    path('home/chat/userMessage/', views.userMessage, name='userMessage'),
    path('home/login/', views.login, name='login'),
    path('home/login/verification/', views.verification, name='verification'),
    path('home/signup/', views.signup, name='signup'),
    path('home/signup/create_user/', views.create_user, name='create_user'),

]

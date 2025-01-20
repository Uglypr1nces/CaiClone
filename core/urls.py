from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/')),  
    path('home/', views.view_characters, name='home'),  
    path('home/get_characters/', views.get_characters, name='get_characters'),
    path('home/create_page/', views.create_page, name='create_page'),  
    path('home/create_page/create_character/', views.create_character, name='create_character'),
    path('home/chat/', views.chat, name='chat'),
    path('home/chat/userMessage/', views.userMessage, name='userMessage'),
    path('home/chat/get_user_messages/', views.get_user_messages, name='get_user_messages'),
    path('home/chat/get_character_messages/', views.get_character_messages, name='get_character_messages'),
    path('home/login/', views.login, name='login'),
    path('home/login/verification/', views.verification, name='verification'),
    path('home/login/get_user_name/', views.get_user_name, name='get_user_name'),
    path('home/signup/', views.signup, name='signup'),
    path('home/signup/create_user/', views.create_user, name='create_user'),

]

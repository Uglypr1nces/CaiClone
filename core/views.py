from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from core.ollama.llama3 import generate_response
from core.ollama.prompt import get_prompt

from core.users.user import *
from core.characters.character import *

from time import sleep
import threading
import json


class PageView(TemplateView):
    template_name = 'home.html'

def create_page(request):
    return render(request, 'create.html')

@csrf_exempt
def create_character(request):
    if request.method == "POST":
        character_name = request.POST.get('name')
        character_description = request.POST.get('description')
        last_id = (0,)
        if get_last_id() is None:
            pass
        else:
            last_id = get_last_id()  
        character = Character(last_id[0] + 1, character_name, character_description)
        character.save_character()

        return HttpResponse("Character created successfully")
    return HttpResponse("Invalid request method", status=405)


@csrf_exempt
def view_characters(request):
    if get_last_id() is None:
        character = Character(1, "temp_name", "temp_description")
        character.delete_character(1)
    else:
        character = Character(get_last_id()[0] + 1, "temp_name", "temp_description")
        character.delete_character(get_last_id()[0] + 1)
    characters = character.print_database() 
    print(characters)
    return render(request, 'home.html', {'characters': characters})

def chat(request):
    return render(request, 'chat.html',)

@csrf_exempt
def userMessage(request):
    if request.method == "POST":
        message = request.POST.get('user_message')
        character_name = request.POST.get('character_name')
        character_description = request.POST.get('character_description')
        prompt = get_prompt(message, character_name, character_description)
        response = generate_response(prompt)
        print(response)
        return HttpResponse(response)
    return HttpResponse("Invalid request method", status=405)

def login(request):
    return render(request, 'login.html')

def verfication(request):
    if request.method == "POST":
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User(password, email)
        user.save_user()
        return HttpResponse("User created successfully")
    return HttpResponse("Invalid request method", status=405)

def create_user(request):
    if request.method == "POST":
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User(password, email)
        user.save_user()
        return HttpResponse("User created successfully")
    return HttpResponse("Invalid request method", status=405)
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

user = User("","")

#/*-----------------------------------------------------------------------*/
#/* -Pages                                                                */
#/*-----------------------------------------------------------------------*/

class PageView(TemplateView):
    template_name = 'home.html'

def create_page(request):
    return render(request, 'create.html')

def chat(request):
    return render(request, 'chat.html',)

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


#/*-----------------------------------------------------------------------*/
#/* -Home Page                                                          */
#/*-----------------------------------------------------------------------*/



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




#/*-----------------------------------------------------------------------*/
#/* -Create Page                                                          */
#/*-----------------------------------------------------------------------*/


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


#/*-----------------------------------------------------------------------*/
#/* -Chat Page                                                            */
#/*-----------------------------------------------------------------------*/

@csrf_exempt
def userMessage(request):
    if request.method == "POST":
        message = request.POST.get('user_message')
        character_name = request.POST.get('character_name')
        character_description = request.POST.get('character_description')
        character_id = request.POST.get('character_id')
        
        # Check if the user is logged in
        if user.email == "" or user.password == "":
            return HttpResponse("User is not logged in", status=403)

        # Add the character and the message
        user.add_character(character_id)
        user.add_message(character_id, message)  # Corrected argument order
        
        # Generate the prompt for the model
        if user.get_messages_for_character(character_id):
            prompt = get_prompt(user.get_messages_for_character(character_id), character_name, character_description)
        else:
            prompt = get_prompt(message, character_name, character_description)

        # Generate response using the prompt
        response = generate_response(prompt)

        # Store the generated response as a message for the character
        user.add_message(character_id, response)

        # Debugging: Print stored messages for this character and database contents
        print(user.get_messages_for_character(character_id))
        print(user.print_database())

        return HttpResponse(response)

    return HttpResponse("Invalid request method", status=405)



#/*-----------------------------------------------------------------------*/
#/* -Login Page                                                           */
#/*-----------------------------------------------------------------------*/


@csrf_exempt
def verification(request):
    if request.method == "POST":
        password = request.POST.get('password')
        email = request.POST.get('email')
        user.update_user(email,password)
        if user.verify_user():
            return HttpResponse("User verified successfully")
        else:
            return HttpResponse("User not found")
    return HttpResponse("Invalid request method", status=405)


#/*-----------------------------------------------------------------------*/
#/* -Sign Up Page                                                           */
#/*-----------------------------------------------------------------------*/


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        password = request.POST.get('password')
        email = request.POST.get('email')
        user.update_user(email,password)
        user.save_user()
        return HttpResponse("User created successfully")
    return HttpResponse("Invalid request method", status=405)
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from time import sleep
import threading
import json

from .characters.character import *

class PageView(TemplateView):
    template_name = 'home.html'

def create_page(request):
    return render(request, 'create.html')

@csrf_exempt
def create_character(request):
    character_name = request.POST.get('name')
    character_description = request.POST.get('description')
    
    last_id = get_last_id()
    character = Character(last_id[0] + 1, character_name, character_description)
    character.save_character()
    character.print_database()

    return HttpResponse('Character created')


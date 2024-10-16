from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from time import sleep
import threading
import json

class page(TemplateView):
    template_name = 'home.html'

def create_page(request):
    return render(request, 'create.html')

def create_character(request):
    print("in development")


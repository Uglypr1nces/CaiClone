from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class page(TemplateView):
    template_name = 'home.html'
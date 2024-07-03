from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World!")

class Index(TemplateView):
    template_name='recipe_book/index.html'
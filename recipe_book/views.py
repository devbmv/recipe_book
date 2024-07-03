from django.views import generic
from .models import Post, Comment
from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World!")


class Index(TemplateView):
    template_name = 'recipe_book/index.html'


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "recipe_book/recipe_list.html"

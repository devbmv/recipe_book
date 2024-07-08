from django.views import generic
from .models import Post, Comment
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "recipe_book/index.html"
    paginate_by = 4
    

def recipe_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "recipe_book/recipe_detail.html",
        {"post": post},
    )

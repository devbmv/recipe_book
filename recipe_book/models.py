from django.db import models
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render, get_object_or_404
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    instructions = models.TextField(blank=False)
    ingredients = models.TextField(blank=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "recipe_list.html"

def profile_page(request):
    user = get_object_or_404(User, username=request.user.username)
    comments = user.commenter.all()

    return render(
        request,
        "profile_page.html",
        {
            "user": user,
            "comments": comments,
        },
    )

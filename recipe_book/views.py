from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "recipe_book/index.html"
    paginate_by = 4


def recipe_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.add_message(
            request, messages.SUCCESS, "Comment submitted and awaiting approval"
        )
    comment_form = CommentForm()

    return render(
        request,
        "recipe_book/recipe_detail.html",
        {
            "post": post,
            "coder": "Mick",
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

from django.views import generic
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "recipe_book/index.html"
    paginate_by = 4


def recipe_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    new_comment = None

    if request.method == "POST":
        print("Received a post request")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )
            comment_form = CommentForm()  # Redefine comment_form to clear the form
    else:
        comment_form = CommentForm()
        print("Resetare variabila commment form")
    return render(
        request,
        "recipe_book/recipe_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "new_comment": new_comment,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
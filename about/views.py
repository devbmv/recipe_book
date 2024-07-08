from django.shortcuts import render

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "about/about.html"
    paginate_by = 4
    

def recipe_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "about/about.html",
        {"post": post,
        "coder":"Matt Rudge",
        }
    )

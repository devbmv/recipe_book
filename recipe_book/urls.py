from .views import PostList
from . import views
from django.urls import path


urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
]

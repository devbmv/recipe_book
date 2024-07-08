from .views import PostList
from . import views
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]

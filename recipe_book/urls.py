from .views import PostList
from . import views
from django.urls import path
from .views import Index


urlpatterns = [
    path('', PostList.as_view(), name='home'),
]

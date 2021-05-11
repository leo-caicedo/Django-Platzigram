# Django
from django.urls import path

# Models
from posts.views import list_posts

app_name = 'posts'
urlpatterns = [
    path('posts', list_posts, name='feed'),
]

from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/',blog_page),
    path('posts/',posts_page)
]
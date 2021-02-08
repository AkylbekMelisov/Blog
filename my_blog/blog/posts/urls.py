from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/',blog_page),
    path('posts/',posts_page),
    path('blogs_p/<int:blog_id>/',blog_post)
]
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Blog, Post


def blog_page(request):
    blogs = Blog.objects.all()
    return render(request,'posts/blog.html',{"blogs":blogs})

def posts_page(request):
    posts = Post.objects.all()
    return render(request,'posts/post.html',{"posts":posts})

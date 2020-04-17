from django.shortcuts import render, get_object_or_404
from .models import Category, Post


# Create your views here.

def index(request):
    posts = Post.objects.order_by('-title')[:2]
    return render(request, 'blog/index.html', {'posts': posts})

def listing(request):
    posts = Post.objects.order_by('-title')
    return render(request, 'blog/listing.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/detail.html', {'post': post})

def add_post(request):
    return render(request, 'blog/add_form.html')
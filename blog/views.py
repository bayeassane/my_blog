from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Post
from .forms import PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def index(request):
    posts = Post.objects.order_by('-created_at')[:2]
    return render(request, 'blog/index.html', {'posts': posts})

def listing(request):
    list_posts = Post.objects.order_by('-created_at')
    paginator = Paginator(list_posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/listing.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/detail.html', {'post': post})

def add_post(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            category = Category.objects.get(name=category)
            image = form.cleaned_data['image']
            new_post = Post.objects.create(
                title=title,
                content=content,
                category=category,
                image=image
            )
            return HttpResponseRedirect(reverse('blog:posts'))

    
    else:
        form = PostForm()
    
    context['form'] = form
    return render(request, 'blog/add_form.html', context)
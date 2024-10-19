from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
from django.db import models
from .models import Author, Tag, Post


def starting_page(request):
    model_posts = Post.objects.all().order_by('-date')[:3]

    return render(request, 'blog/index.html', {
        'posts': model_posts
    })

def posts(request):
    model_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'all_posts': model_posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tag': identified_post.tag.all()
    })

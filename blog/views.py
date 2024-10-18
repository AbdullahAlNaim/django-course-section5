from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
from django.db import models

all_posts = [
    {
        'slug': 'hiking-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'Abdullah',
        'date': date(2024, 10, 13),
        'title': 'Mountain Hiking',
        'exerpt': 'Nothing like hiking in the mountains. It was so cool',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. """
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.jpg',
        'author': 'Abdullah',
        'date': date(2024, 10, 14),
        'title': 'Programming is great',
        'exerpt': 'I love coding and build stuff and making lots of money.',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. """
    },
    {
        'slug': 'Exercising',
        'image': 'woods.jpg',
        'author': 'Abdullah',
        'date': date(2024, 10, 14),
        'title': 'Programming is great',
        'exerpt': 'I love coding and build stuff and making lots of money.',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis iaculis ante sapien. Praesent in lacinia urna. Praesent ultricies vulputate consequat. Morbi viverra elementum sapien, ut dapibus ligula congue vel. Integer malesuada placerat mi, id eleifend libero placerat at. Nam faucibus nulla vitae finibus vulputate. Quisque interdum ut. """
    },
]

def get_date(posts):
    return posts['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })

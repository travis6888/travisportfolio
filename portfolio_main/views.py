from django.shortcuts import render

# Create your views here.
from mezzanine.blog.models import BlogPost


def home(request):
    return render(request, 'pages/home.html')

def landing(request):
    return render(request, 'pages/newlanding.html')


def projects(request):
    return render(request, 'pages/projects.html')


def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog_post_list.html', {'blog_posts': blog_posts})


def resume(request):
    return render(request, 'pages/resume.html')
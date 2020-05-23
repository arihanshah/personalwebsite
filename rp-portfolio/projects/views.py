from django.shortcuts import render
from projects.models import Project
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def single_blog(request):
    return render(request, 'blog-single.html')
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def blog(request):
    blogs= Blog.objects.all()
    return render (request, "blog/blog.html",{'blogs':blogs})

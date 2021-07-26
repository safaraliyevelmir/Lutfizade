from django.shortcuts import render
from .models import Blog


def BlogPageView(request):
    blogs = Blog.objects.all
    context = {
        'blogs':blogs
    }
    return render(request,'blog.html',context)

def BlogSinglePageView(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog
    }
    return render(request,'blogdetail.html',context)
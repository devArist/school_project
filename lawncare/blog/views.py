from django.shortcuts import render
from . import models

# Create your views here.
def blog(request):
    blogs = models.Blog.objects.filter(status=True).order_by('-date_update')
    return render(request, 'blog/blog.html', locals())

def detail(request, pk):
    blog = models.Blog.objects.get(pk=pk)
    return render(request, 'blog/blog-single.html', locals())
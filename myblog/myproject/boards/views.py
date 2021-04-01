from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from django.utils import timezone

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def post_list(request):
    return render(request, 'boards/post_list.html', {})
    #render (put together) our template

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'boards/post_list.html', {'posts':posts})

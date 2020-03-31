from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def Index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})


def post(request):
    return HttpResponse('I\'m the single post page.')
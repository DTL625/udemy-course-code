from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def Index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})


def post(request, slug):
    pst = get_object_or_404(Post, slug=slug)
    print(slug)
    print(pst)

    return render(request, 'post.html', {'post_item': pst})


def about(request):
    return render(request, 'about.html')
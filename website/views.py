from django.shortcuts import render
from.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def single(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single.html', {'post': post})


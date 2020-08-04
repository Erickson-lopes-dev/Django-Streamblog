from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from.models import Post


def home(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return render(request, 'blog/home.html')


def django_logout(request):
    logout(request)
    return redirect('/')


def single(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single.html', {'post': post})


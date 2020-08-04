from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    return render(request, 'registration/login.html', {'message': f'Usuário criado com sucesso {user}'})


def django_login(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'posts': posts})
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return render(request, 'blog/home.html', {'posts': posts})


@login_required(login_url='/login/')
def django_logout(request):
    logout(request)
    return redirect('/')


def single(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single.html', {'post': post})

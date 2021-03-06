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
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    try:
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

    except Exception:
        return render(request, 'registration/register.html',
                      {'message': f'Não foi possível criar um novo usuário', 'username': username, 'email': email, })
    else:
        if user:
            return render(request, 'registration/login.html',
                          {'message': f'Olá, {user.username} você foi registrado com sucesso!'})


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

    return render(request, 'registration/login.html', {'message': 'Usuário não existe'})


def single(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single.html', {'post': post})


@login_required(login_url='/login/')
def django_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def my_posts(request):
    posts = Post.objects.filter(user=request.user.id)
    return render(request, 'blog/mypost.html', {'posts': posts})


@login_required(login_url='/login/')
def create(request):
    if request.POST:
        Post.objects.create(
            title=request.POST['title'],
            sub_title=request.POST['sub_title'],
            content=request.POST['content'],
            user=request.user
        )
        return render(request, 'blog/create.html', {'message': 'Salvo com sucesso'})
    return render(request, 'blog/create.html')


@login_required(login_url='/login/')
def edit(request, pk):
    if request.method == "GET":
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/edit.html', {"post": post})

    post = Post.objects.filter(pk=pk).update(
        title=request.POST['title'],
        sub_title=request.POST['sub_title'],
        content=request.POST['content'],
        user=request.user
    )
    return render(request, 'blog/edit.html', {"post": Post.objects.get(pk=pk), 'message': 'Atualizado!'})


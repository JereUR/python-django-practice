from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Service


def formCounter(request):
    return render(request, 'formCounter.html')


def counter(request):
    if request.method == 'POST':
        text = request.POST['text']
        amount_of_words = len(text.split())
        posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
        return render(request, 'counter.html', {'amount': amount_of_words, 'posts': posts})
    else:
        posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
        return render(request, 'counter.html', {'amount': None, 'posts': posts})


def static(request):
    return render(request, 'static.html')


def index(request):
    services = Service.objects.all()

    return render(request, 'index.html', {'services': services})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Passwords Do Not Match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

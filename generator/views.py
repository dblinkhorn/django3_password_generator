from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'as08q24tg7hag'})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    the_password = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+{}|<>?~'))

    for char in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')

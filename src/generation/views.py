from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generation/home.html')


def password(request):
    charactes = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        charactes.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        charactes.extend(list('!@#$%^&*()_'))
    if request.GET.get('numbers'):
        charactes.extend(list('1234567890'))

    length = int(request.GET.get('lenght'))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(charactes)

    return render(request, 'generation/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generation/about.html')


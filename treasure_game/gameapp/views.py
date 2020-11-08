from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import UserForm
from .forms import UserForm

def index(request):
    if request.method == "POST":
        name = request.POST.get("login")
        password = request.POST.get("password")
        with open("Rediska.txt", "w+") as f:
            f.write('rediska name {} password {}'.format(name, password))

        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}, your password is {1}</h2>".format(name, password))
    else:
        userform = UserForm()
        return render(request, "login.html", {"form": userform})

def start_game(request):
    return HttpResponse('game.html')
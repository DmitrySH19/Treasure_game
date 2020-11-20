from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import UserForm
from .forms import UserForm

def start_game(request, game_room):
    return render(request, 'game.html', {
        'game_room': game_room
    })

from django.urls import path
from django.conf.urls import include
from django.urls import path, re_path
from gameapp import views
from django.conf.urls import url

urlpatterns = [
    path('<str:game_room>/', views.start_game),
]
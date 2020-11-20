from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'login/', include('gameapp.urls')),
    url(r'^registration/$', views.register, name='register'),
]
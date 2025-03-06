# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_personagem, name='base_personagem'),
]
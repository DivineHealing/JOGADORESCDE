# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_personagem, name='exibir_personagem'),
]
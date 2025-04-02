# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_personagem, name='base_personagem'),
    path('salvar_base_personagem', views.salvar_base_personagem, name='salvar_base_personagem'),

]
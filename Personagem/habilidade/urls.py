# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('habilidade/', views.habilidade, name='habilidade'),
    path('salvar_habilidade', views.salvar_habilidade, name='salvar_habilidade'),

]
# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.habilidade, name='habilidade'),
    path('<int:personagem_id>/', views.habilidade, name='habilidade'),
    path('salvar_habilidade', views.salvar_habilidade, name='salvar_habilidade'),

]
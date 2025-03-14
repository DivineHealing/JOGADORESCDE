# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_personagem, name='exibir_personagem'),
    path('<int:personagem_id>/', views.exibir_personagem, name='exibir_personagem_id'),  # URL com ID
    path('personagens/<int:personagem_id>/criar_peca/', views.criar_peca_armadura, name='criar_peca_armadura'),
]
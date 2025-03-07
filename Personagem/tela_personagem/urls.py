# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_personagem, name='exibir_personagem'),
    path('personagem/<int:personagem_id>/', views.exibir_personagem, name='exibir_personagem_id'),  # URL com ID
]
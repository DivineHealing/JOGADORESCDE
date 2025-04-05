# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_personagem, name='exibir_personagem'),
    path('<int:personagem_id>/', views.exibir_personagem, name='exibir_personagem_id'),  # URL com ID
    path('cadastrar_personagem', views.cadastrar_personagem, name='cadastrar_personagem'),    
    path('deletar_personagem', views.deletar_personagem, name='deletar_personagem')
]
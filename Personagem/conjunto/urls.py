# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.conjunto, name='conjunto'),
    path('<str:tipo>/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('lista/', views.lista_equipamentos, name='lista_equipamentos'),
]
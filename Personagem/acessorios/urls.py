# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acessorios, name='acessorios'),
    path('atributos/<str:tipo>/', views.cadastrar_equipamento_acessorios, name='cadastrar_atributos_acessorios'),
    path('efeitos/<str:tipo>/', views.cadastrar_efeitos_acessorios, name='cadastrar_efeitos_acessorios'),
]
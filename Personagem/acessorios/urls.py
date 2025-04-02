# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acessorios, name='acessorios'),
    path('atributos/<str:tipo>/', views.cadastrar_equipamento_acessorios, name='cadastrar_atributos_acessorios'),
    path('efeitos/<str:tipo>/', views.cadastrar_efeitos_acessorios, name='cadastrar_efeitos_acessorios'),
    path('salvar_acessorio_efeitos', views.salvar_acessorio_efeitos, name='salvar_acessorio_efeitos'),
    path('salvar_acessorio_atributos', views.salvar_acessorio_atributos, name='salvar_acessorio_atributos'),

]
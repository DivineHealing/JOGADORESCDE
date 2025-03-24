# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.conjunto, name='conjunto'),
    path('atributos/<str:tipo>/', views.cadastrar_equipamento, name='cadastrar_atributos'),
    path('efeitos/<str:tipo>/', views.cadastrar_efeitos, name='cadastrar_efeitos'),
    path('', views.perfil, name='perfil')
]
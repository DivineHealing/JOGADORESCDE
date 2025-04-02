# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.conjunto, name='conjunto'),
    path('atributos/<str:tipo>/', views.cadastrar_equipamento, name='cadastrar_atributos_conjunto'),
    path('efeitos/<str:tipo>/', views.cadastrar_efeitos, name='cadastrar_efeitos_conjunto'),
    path('', views.perfil, name='perfil'),
    path('salvar_conjunto_efeitos', views.salvar_conjunto_efeitos, name='salvar_conjunto_efeitos'),
    path('salvar_conjunto_atributo', views.salvar_conjunto_atributo, name='salvar_conjunto_atributo'),
]
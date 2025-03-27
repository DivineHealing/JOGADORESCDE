# tela_personagens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.arma, name='arma'),
    path('atributos/<str:tipo>/', views.cadastrar_equipamento_armas, name='cadastrar_atributos_arma'),
    path('efeitos/<str:tipo>/', views.cadastrar_efeitos_armas, name='cadastrar_efeitos_arma'),
]
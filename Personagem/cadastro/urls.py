from django.urls import path
from .views import cadastro
from . import views

urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('maestria/<str:tipo>/', views.cadastrar_maestria, name='cadastrar_maestria'),
    path('salvar_arma_atributo', views.salvar_maestria_atributo, name='salvar_maestria_atributo')
]
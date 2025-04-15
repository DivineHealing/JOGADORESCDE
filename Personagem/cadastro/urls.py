from django.urls import path
from .views import cadastro
from . import views

urlpatterns = [
    path('<int:personagem_id>/', views.cadastro, name="cadastro"),
    path('maestria/<int:personagem_id>/<str:tipo>/', views.cadastrar_maestria, name='cadastrar_maestria'),
    path('salvar_maestria_atributo', views.salvar_maestria_atributo, name='salvar_maestria_atributo')
]
from django.urls import path
from .views import inicio, somarteste, lista_cadastros
from . import views

urlpatterns = [
    #path('', views.lista_cadastros, name="lista_cadastros")
    path('', somarteste)
]

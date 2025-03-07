from django.urls import path
from .views import cadastro
from . import views

urlpatterns = [
    path('', views.cadastro, name="cadastro")
]

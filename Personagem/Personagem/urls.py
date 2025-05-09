"""
URL configuration for Personagem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py pasta raiz
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Acesso a tela de Administração do Banco.
    path('cadastro/', include('cadastro.urls'), name="cadastro"), # Acesso a tela de Cadastro.
    path('conjunto/', include('conjunto.urls'), name="conjunto"), # Acesso a tela de Conjunto.
    path('arma/', include('arma.urls'), name="arma"), # Acesso a tela de Arma.
    path('acessorios/', include('acessorios.urls'), name="acessorios"), # Acesso a tela de Acessorios.
    path('base/', include('base_personagem.urls'), name="base"), # Acesso ao Cadastro de Informações Base do Personagem.
    path('habilidade/', include('habilidade.urls'), name="habilidade"), # Acesso a criação de Habilidades do Personagem
    path('', include('tela_personagem.urls'), name="home"),  # Acesso a tela de Informações.
]

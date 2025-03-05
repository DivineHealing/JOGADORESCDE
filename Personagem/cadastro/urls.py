from django.urls import path
from .views import soma_view
from . import views

urlpatterns = [
    path('', views.soma_view, name="soma_view")
    #path('', somarteste)
]

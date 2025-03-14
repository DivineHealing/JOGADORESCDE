from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register(r'personagens', views.PersonagemViewSet, basename='personagem')  # Adicionei basename='personagem'

personagens_router = routers.NestedSimpleRouter(router, r'personagens', lookup='personagem')
personagens_router.register(r'conjuntos', views.ConjuntoArmaduraViewSet, basename='personagem-conjuntos')

conjuntos_router = routers.NestedSimpleRouter(personagens_router, r'conjuntos', lookup='conjunto')
conjuntos_router.register(r'(?P<tipo>elmo|peitoral|manoplas|calcas|botas)', views.PecaArmaduraViewSet, basename='conjunto-pecas')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(personagens_router.urls)),
    path('', include(conjuntos_router.urls)),
]
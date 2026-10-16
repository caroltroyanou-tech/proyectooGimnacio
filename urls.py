from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntrenadorViewSet, PlanViewSet, SocioViewSet

# Instancia del Router global
router = DefaultRouter()
router.register(r'entrenador', EntrenadorViewSet, basename='entrenador')
router.register(r'planes', PlanViewSet, basename='plan')
router.register(r'socios', SocioViewSet, basename='socio')

urlpatterns = [
    # Endpoints de la API unificada
    path('api/', include(router.urls)),
]

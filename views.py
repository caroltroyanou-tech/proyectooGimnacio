from rest_framework import viewsets
from .models import Entrenador, Plan, Socio
from .serializers import EntrenadorSerializer, PlanSerializer, SocioSerializer

class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

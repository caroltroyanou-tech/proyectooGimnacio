rom rest_framework import serializers
from .models import Entrenador, Plan, Socio

class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class SocioSerializer(serializers.ModelSerializer):
    # Permite visualizar detalles completos de las relaciones al consultar
    nombre_plan = serializers.ReadOnlyField(source='plan_asignado.nombre_plan')
    nombre_entrenador = serializers.ReadOnlyField(source='entrenador_personal.nombre')

    class Meta:
        model = Socio
        fields = ['id', 'nombre', 'apellido', 'fecha_inscripcion', 'plan_asignado', 'entrenador_personal', 'nombre_plan', 'nombre_entrenador']

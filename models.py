from django.db import models

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Entrenador: {self.nombre}"

class Plan(models.Model):
    nombre_plan = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_dias = models.IntegerField(help_text="Duración de la membresía en días")

    def __str__(self):
        return f"{self.nombre_plan} - ${self.precio}"

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    plan_asignado = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="socios")
    entrenador_personal = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Socio: {self.nombre} {self.apellido}"
    

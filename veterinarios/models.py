from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Veterinario")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cuenta de usuario")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self): return self.nombre

class Horarios(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name="Veterinario")

    # Horarios son listas de booleanos de los bloques de horario del día. Cada bloque es de 30 mins por 8 horas.
    lunes = ArrayField(models.BooleanField(default=False), size=16)
    martes = ArrayField(models.BooleanField(default=False), size=16)
    miercoles = ArrayField(models.BooleanField(default=False), size=16)
    jueves = ArrayField(models.BooleanField(default=False), size=16)
    viernes = ArrayField(models.BooleanField(default=False), size=16)
    sabado = ArrayField(models.BooleanField(default=False), size=16)
    domingo = ArrayField(models.BooleanField(default=False), size=16)

    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")
    def __str__(self): return f"Horario de Veterinario {self.veterinario}"
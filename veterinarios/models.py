from django.db import models

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Veterinario")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self): return self.nombre
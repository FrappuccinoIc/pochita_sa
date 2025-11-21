from django.db import models
from ..veterinarios.models import Veterinario
from ..fichas_mascota.models import FichaMascota

ESTADOS_DE_CITA = [
    ("pendiente", "Pendiente"),
    ("realizado", "Realizado"),
    ("cancelado", "Cancelado")
]

class Cita(models.Model):
    fecha = models.DateField(verbose_name="Fecha agendada")
    hora_inicial = models.IntegerField(max_length=2, verbose_name="Bloque inicial de cita")
    hora_final = models.IntegerField(max_length=2, verbose_name="Bloque final de cita")
    estado = models.CharField(choices=ESTADOS_DE_CITA, verbose_name="Estado")

    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name="Veterinario asignado")
    ficha_cliente = models.ForeignKey(FichaMascota, on_delete=models.CASCADE, verbose_name="Ficha Cliente")

    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")

    def __str__(self): return f"Cita para {self.fecha}"
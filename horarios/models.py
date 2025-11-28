from django.db import models
from veterinarios.models import Veterinario
from fichas_mascota.models import FichaMascota
from datetime import timedelta, time, datetime

ESTADOS_DE_CITA = [
    ("pendiente", "Pendiente"),
    ("realizado", "Realizado"),
    ("cancelado", "Cancelado")
]

class Cita(models.Model):
    fecha = models.DateField(verbose_name="Fecha agendada")
    hora_inicial = models.IntegerField(verbose_name="Bloque inicial de cita")
    hora_final = models.IntegerField(verbose_name="Bloque final de cita")
    estado = models.CharField(max_length=9, choices=ESTADOS_DE_CITA, verbose_name="Estado")

    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name="Veterinario asignado")
    ficha_cliente = models.ForeignKey(FichaMascota, on_delete=models.CASCADE, verbose_name="Ficha Cliente")

    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")

    def bloques_a_tiempo(self, bloque):
        inicio_horario = datetime(self.fecha.year, self.fecha.month, self.fecha.day, 8, 0, 0, 0)
        result = inicio_horario + timedelta(minutes=(bloque - 1) * 30)
        return result.strftime('%H:%M')

    @property
    def hora_inicial_a_tiempo(self):
        return self.bloques_a_tiempo(self.hora_inicial)

    @property
    def hora_final_a_tiempo(self):
        return self.bloques_a_tiempo(self.hora_final)

    def __str__(self): return f"Cita para {self.fecha}"
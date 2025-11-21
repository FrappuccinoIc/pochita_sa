from django.db import models

class FichaMascota(models.Model):
    cliente = models.CharField(max_length=90, verbose_name="Nombre del dueño")
    mascota = models.CharField(max_length=30, verbose_name="Nombre de la mascota")
    especie = models.CharField(max_length=40, verbose_name="Especie de la mascota")
    edad = models.IntegerField(verbose_name="Edad de la mascota")
    peso = models.IntegerField(verbose_name="Peso de la mascota")

    vacunas = models.TextField(max_length=60, verbose_name="Descripción de vacunas")
    tratamientos_apli = models.TextField(max_length=200, verbose_name="Tratamientos aplicados")
    tratamientos_sig = models.TextField(max_length=100, verbose_name="Siguiente tratamiento por aplicar")

    telefono = models.CharField(max_length=15, verbose_name="Teléfono de contacto")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")

    def __str__(self): return f"Ficha de {self.mascota}"
from django.db import models
from django.contrib.auth.models import User
from django_jsonform.models.fields import ArrayField
from django_jsonform.models.fields import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Recepcionista(models.Model):
    nombre = models.CharField(max_length=120, verbose_name="Nombre de Recepcionista")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cuenta de usuario")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self): return self.nombre

class Veterinario(models.Model):
    nombre = models.CharField(max_length=120, verbose_name="Nombre de Veterinario")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cuenta de usuario")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self): return self.nombre

def default_dia():
    return {
        'bloque1': False,
        'bloque2': False,
        'bloque3': False,
        'bloque4': False,
        'bloque5': False,
        'bloque6': False,
        'bloque7': False,
        'bloque8': False,
        'bloque9': False,
        'bloque10': False,
        'bloque11': False,
        'bloque12': False,
        'bloque13': False,
        'bloque14': False,
        'bloque15': False,
        'bloque16': False,
    }

class Horario(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name="Veterinario")

    # Horarios son listas de booleanos de los bloques de horario del día. Cada bloque es de 30 mins por 8 horas.

    HORARIO_SCHEMA = {
        'type': 'object',
        'keys': {
            'bloque1': {'type': 'boolean', 'default': False, 'title': '8:00 - 8:30'},
            'bloque2': {'type': 'boolean', 'default': False, 'title': '8:30 - 9:00'},
            'bloque3': {'type': 'boolean', 'default': False, 'title': '9:00 - 9:30'},
            'bloque4': {'type': 'boolean', 'default': False, 'title': '9:30 - 10:00'},
            'bloque5': {'type': 'boolean', 'default': False, 'title': '10:00 - 10:30'},
            'bloque6': {'type': 'boolean', 'default': False, 'title': '10:30 - 11:00'},
            'bloque7': {'type': 'boolean', 'default': False, 'title': '11:00 - 11:30'},
            'bloque8': {'type': 'boolean', 'default': False, 'title': '11:30 - 12:00'},
            'bloque9': {'type': 'boolean', 'default': False, 'title': '12:00 - 12:30'},
            'bloque10': {'type': 'boolean', 'default': False, 'title': '12:30 - 13:00'},
            'bloque11': {'type': 'boolean', 'default': False, 'title': '13:00 - 13:30'},
            'bloque12': {'type': 'boolean', 'default': False, 'title': '13:30 - 14:00'},
            'bloque13': {'type': 'boolean', 'default': False, 'title': '14:00 - 14:30'},
            'bloque14': {'type': 'boolean', 'default': False, 'title': '14:30 - 15:00'},
            'bloque15': {'type': 'boolean', 'default': False, 'title': '15:00 - 15:30'},
            'bloque16': {'type': 'boolean', 'default': False, 'title': '15:30 - 16:00'}
        },
    }

    BLOQUES_A_HORAS = {
    'bloque1': '08:00 - 08:30',
    'bloque2': '08:30 - 09:00',
    'bloque3': '09:00 - 09:30',
    'bloque4': '09:30 - 10:00',
    'bloque5': '10:00 - 10:30',
    'bloque6': '10:30 - 11:00',
    'bloque7': '11:00 - 11:30',
    'bloque8': '11:30 - 12:00',
    'bloque9': '12:00 - 12:30',
    'bloque10': '12:30 - 13:00',
    'bloque11': '13:00 - 13:30',
    'bloque12': '13:30 - 14:00',
    'bloque13': '14:00 - 14:30',
    'bloque14': '14:30 - 15:00',
    'bloque15': '15:00 - 15:30',
    'bloque16': '15:30 - 16:00'
    }

    lunes = JSONField(schema=HORARIO_SCHEMA, default=default_dia)
    martes = JSONField(schema=HORARIO_SCHEMA, default=default_dia)
    miercoles = JSONField(schema=HORARIO_SCHEMA, default=default_dia)
    jueves = JSONField(schema=HORARIO_SCHEMA, default=default_dia)
    viernes = JSONField(schema=HORARIO_SCHEMA, default=default_dia)
    sabado = JSONField(schema=HORARIO_SCHEMA, default=default_dia)
    domingo = JSONField(schema=HORARIO_SCHEMA, default=default_dia)

    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")
    
    
    def __str__(self): return f"Horario de Veterinario {self.veterinario}"
    
    def get_disponibles(self, dia_nombre):
        """dia_nombre = 'lunes', 'martes', etc"""
        dia = getattr(self, dia_nombre)
        disponibles = []
        for bloque, valor in dia.items():
            if valor is True:
                disponibles.append(self.BLOQUES_A_HORAS[bloque])
        return disponibles

@receiver(post_save, sender=Veterinario)
def crear_horario_veterinario(sender, instance, created, **kwargs):
    if created:
        Horario.objects.create(veterinario=instance)
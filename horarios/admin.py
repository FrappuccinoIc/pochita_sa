from django.contrib import admin
from .models import Cita

class CitaAdmin(admin.ModelAdmin):
    readonly_fields=('ficha_cliente','updated')
    list_display=('ficha_cliente__cliente', 'veterinario__nombre', 'fecha')
    ordering=('fecha', 'hora_incial', 'estado')
    search_fields=('ficha_cliente__cliente', 'veterinario__nombre')
    list_filter=('estado', 'fecha')

admin.register(Cita, CitaAdmin)
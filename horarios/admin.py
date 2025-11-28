from django.contrib import admin
from .models import Cita

class CitaAdmin(admin.ModelAdmin):
    #readonly_fields=('ficha_cliente','updated')
    list_display=('get_nombre_cliente', 'get_nombre_veterinario', 'fecha')
    ordering=('fecha', 'hora_inicial', 'estado')
    search_fields=('get_nombre_cliente', 'get_nombre_veterinario')
    list_filter=('estado', 'fecha')

    def get_nombre_cliente(self, obj): return obj.ficha_cliente.cliente

    get_nombre_cliente.admin_order_field = 'ficha_cliente__cliente'
    get_nombre_cliente.short_description = 'Nombre Cliente'

    def get_nombre_veterinario(self, obj): return obj.veterinario.nombre

    get_nombre_veterinario.admin_order_field = 'veterinario__nombre'
    get_nombre_veterinario.short_description = 'Nombre Veterinario'

admin.site.register(Cita, CitaAdmin)
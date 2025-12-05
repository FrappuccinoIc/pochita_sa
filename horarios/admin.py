from django.contrib import admin
from .models import Cita, Notificacion

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

class NotificacionAdmin(admin.ModelAdmin):
    list_display=('get_username_recepcionista', 'get_cita_veterinario', 'get_cita_mascota', 'created')

    def get_username_recepcionista(self, obj): return obj.recepcionista.usuario

    get_username_recepcionista.admin_order_field = 'recepcionista__usuario'
    get_username_recepcionista.short_description = 'Recepcionista'

    def get_cita_veterinario(self, obj): return obj.cita.veterinario.nombre

    get_cita_veterinario.admin_order_field = 'cita__veterinario__nombre'
    get_cita_veterinario.short_description = 'Veterinario de cita cancelada'

    def get_cita_mascota(self, obj): return obj.cita.ficha_cliente.mascota

    get_cita_mascota.admin_order_field = 'cita__ficha_cliente__mascota'
    get_cita_mascota.short_description = 'Mascota'

admin.site.register(Cita, CitaAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
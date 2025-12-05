from django.contrib import admin
from .models import Recepcionista, Veterinario, Horario

class RecepcionistaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'usuario', 'created')
    ordering=('created', 'nombre', 'usuario')
    search_fields=('nombre', '')

class VeterinarioAdmin(admin.ModelAdmin):
    list_display=('nombre', 'usuario', 'created')
    ordering=('created', 'nombre', 'usuario')
    search_fields=('nombre', '')

class HorarioAdmin(admin.ModelAdmin):
    list_display=('veterinario', 'updated')
    """ ordering=('updated', 'veterinario')
    search_fields=('veterinario', '') """

admin.site.register(Recepcionista, RecepcionistaAdmin)
admin.site.register(Veterinario, VeterinarioAdmin)
admin.site.register(Horario, HorarioAdmin)
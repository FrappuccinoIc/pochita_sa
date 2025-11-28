from django.contrib import admin
from .models import Veterinario,Horario

class VeterinarioAdmin(admin.ModelAdmin):
    list_display=('nombre', 'usuario', 'created')
    ordering=('created', 'nombre', 'usuario')
    search_fields=('nombre', '')

class HorarioAdmin(admin.ModelAdmin):
    list_display=('veterinario', 'updated')
    """ ordering=('updated', 'veterinario')
    search_fields=('veterinario', '') """

admin.site.register(Veterinario, VeterinarioAdmin)
admin.site.register(Horario, HorarioAdmin)
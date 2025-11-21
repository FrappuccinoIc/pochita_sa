from django.contrib import admin
from .models import FichaMascota

class FichaMascotaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('mascota', 'cliente', 'telefono', 'created')
    ordering=('created', 'mascota')
    search_fields=('mascota', 'cliente', 'especie', 'telefono')

admin.site.register(FichaMascota, FichaMascotaAdmin)
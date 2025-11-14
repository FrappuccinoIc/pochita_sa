from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = "vet_create"),

    path('perfil/<int:veterinario_id>/', views.perfil, name = "vet_perfil"),
    path('perfil/<int:veterinario_id>/edit/', views.edit, name = "vet_edit"),
    
    path('perfil/<int:veterinario_id>/horario_edit/', views.horario_edit, name = "vet_horario_edit"),
]
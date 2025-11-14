from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name = "create"),
    path('create/', views.create, name = "create"),

    path('perfil/<int:veterinario_id>/', views.perfil, name = "perfil"),
    path('perfil/<int:veterinario_id>/edit/', views.edit, name = "edit"),
    
    path('horario/<int:veterinario_id>', views.horario, name = "horario"),
    path('horario/<int:veterinario_id>/edit/', views.horario_edit, name = "horario_edit"),
]
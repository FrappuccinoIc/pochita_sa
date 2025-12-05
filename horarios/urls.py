from django.urls import path
from . import views

urlpatterns = [
    path('', views.horarios, name = "horarios"),
    path('citas/registrar', views.registrar_cita, name = "registrar_cita"),
    path('<int:veterinario_id>/', views.vet_disponibilidad, name = "disponibilidad_vet"),
    path('eliminar/<int:cita_id>/', views.eliminar_cita, name="eliminar_cita"),
]
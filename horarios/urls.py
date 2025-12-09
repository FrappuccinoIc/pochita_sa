from django.urls import path
from . import views

urlpatterns = [
    path('', views.horarios, name = "horarios"),
    path('citas/registrar/confirmar/', views.vet_confirmar, name = "vet_confirmar"),
    path('citas/registrar/', views.registrar_cita, name = "registrar_cita"),
    path('notificaciones/', views.ver_notificaciones, name = "notificaciones"),
    path('<int:veterinario_id>/', views.vet_disponibilidad, name = "disponibilidad_vet"),
    path('eliminar/<int:cita_id>/', views.eliminar_cita, name="eliminar_cita"),
    path('restringido/', views.restringido, name="restringido"),
    path('api/horas-disponibles/', views.horas_disponibles, name='horas_disponibles')

]
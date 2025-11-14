from django.urls import path
from . import views

urlpatterns = [
    path('', views.horarios, name = "horarios"),
    path('<int:veterinario_id>/', views.vet_disponibilidad, name = "disponibilidad_vet"),
]
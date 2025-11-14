from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil, name = "perfil"),
    path('edit/', views.edit, name = "perfil"),
    path('horario/', views.horario, name = "horario"),
    path('horario/edit/', views.horario_edit, name = "horario_edit"),
]
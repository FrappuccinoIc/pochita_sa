from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = "ficha_create"),
    path('detalle/<int:veterinario_id>/', views.detalle, name = "ficha_detalle"),
    path('edit/<int:veterinario_id>/', views.edit, name = "ficha_edit"),
]
from django.shortcuts import render, get_object_or_404
from .models import FichaMascota

def index(req):
    mascotas = FichaMascota.objects.all()
    return render(req, 'fichas_mascota/index.html', {'mascotas': mascotas})

def create(req):
    return render(req, 'fichas_mascota/create.html')

def detalle(req, veterinario_id):
    ficha = get_object_or_404(FichaMascota, id=veterinario_id)
    return render(req, 'fichas_mascota/detalle.html', {'ficha': ficha})

def edit(req, veterinario_id):
    ficha = get_object_or_404(FichaMascota, id=veterinario_id)
    return render(req, 'fichas_mascota/edit.html', {'ficha': ficha})
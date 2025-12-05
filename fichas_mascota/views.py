from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FichaMascota

@login_required
def index(req):
    mascotas = FichaMascota.objects.all()
    return render(req, 'fichas_mascota/index.html', {'mascotas': mascotas})

@login_required
def create(req):
    return render(req, 'fichas_mascota/create.html')

@login_required
def detalle(req, veterinario_id):
    ficha = get_object_or_404(FichaMascota, id=veterinario_id)
    return render(req, 'fichas_mascota/detalle.html', {'ficha': ficha})

@login_required
def edit(req, veterinario_id):
    ficha = get_object_or_404(FichaMascota, id=veterinario_id)
    return render(req, 'fichas_mascota/edit.html', {'ficha': ficha})
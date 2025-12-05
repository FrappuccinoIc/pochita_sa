from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CitaForm
from django.utils.timezone import localtime
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar
from .models import Cita
from veterinarios.models import Veterinario

@login_required
def horarios(req):
    veterinario = req.GET.get('veterinario')
    if veterinario:
        veterinario = veterinario.strip()

    estado = req.GET.get('estado', None)
    lista_estados = ["realizado", "pendiente", "cancelado"]
    if estado not in lista_estados: estado = "pendiente"

    fecha = localtime().date()
    try: 
        lista_fecha = req.GET.get('fecha', None).split('-')
        for i in range(3):
            lista_fecha[i] = int(lista_fecha[i])
        fecha = date(lista_fecha[0], lista_fecha[1], lista_fecha[2])
        fecha_max = fecha
    except: 
        fecha = date(fecha.year, fecha.month, 1)
        fecha_max = fecha + relativedelta(months=1)
        fecha_max = date(fecha_max.year, fecha_max.month, calendar.monthrange(fecha_max.year, fecha_max.month)[1])

    if(veterinario): citas = Cita.objects.filter(fecha__range = (fecha, fecha_max), estado = estado, veterinario__id = veterinario).order_by('fecha')
    else: citas = Cita.objects.filter(fecha__range = (fecha, fecha_max), estado = estado).order_by('fecha')

    citas_canceladas = Cita.objects.filter(estado = "cancelado")

    veterinarios = Veterinario.objects.all().order_by('id')

    return render(req, 'horarios/horario.html', {
        'citas': citas,
        "citas_canceladas": citas_canceladas,
        'fecha_min': date(2020, 1, 1),
        'fecha_max': fecha_max,
        'veterinarios': veterinarios
    })

@login_required
def registrar_cita(req):
    cita_form = CitaForm()
    if req.method == "POST":
        cita_form = CitaForm(data = req.POST)
        if cita_form.is_valid():
            cita_form.save()
            return redirect(reverse('registrar_cita') + '?ok')

    return render(req, 'horarios/crear_cita.html', {"form": cita_form})

@login_required
def vet_disponibilidad(req):
    return render(req, 'horarios/horarios.html')
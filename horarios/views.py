from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from .models import Cita
from veterinarios.models import Veterinario

def horarios(req):
    veterinario = ""
    try: veterinario = req.GET.get('veterinario').trim()
    except: pass

    estado = req.GET.get('estado')
    lista_estados = ["realizado", "pendiente", "cancelado"]
    if estado not in lista_estados: estado = "pendiente"

    lista_fecha = req.GET.get('fecha').split('-')
    try: 
        for i in range(3):
            lista_fecha[i] = int(lista_fecha[i])
        fecha = date(lista_fecha[0], lista_fecha[1], lista_fecha[2])
    except: fecha = localtime().date()
    fecha_max = fecha + relativedelta(months=1)
    fecha_max = date(fecha_max.year, fecha_max.month, calendar.monthrange(fecha_max.year, fecha_max.month)[1])

    if(veterinario): citas = Cita.objects.filter(fecha__range = (fecha, fecha), estado = estado, veterinario = veterinario)
    else: citas = Cita.objects.filter(fecha__range = (fecha, fecha), estado = estado)

    return render(req, 'horarios/horario.html', {
        'citas': citas,
        'fecha_min': date(fecha.year, fecha.month, 1),
        'fecha_max': fecha_max
    })

def vet_disponibilidad(req):
    return render(req, 'horarios/horarios.html')
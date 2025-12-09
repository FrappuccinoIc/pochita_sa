from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.urls import reverse
from .forms import CitaForm
from django.utils.timezone import localtime
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from .models import Cita, Notificacion
from veterinarios.models import Veterinario, Recepcionista, Horario
from core.views import get_notificaciones
from django.http import JsonResponse

@login_required
def horarios(req):
    veterinario = req.GET.get('veterinario')
    if veterinario:
        veterinario = veterinario.strip()

    estado = req.GET.get('estado', None)
    lista_estados = ["realizado", "pendiente", "cancelado"]
    if estado not in lista_estados:
        estado = "pendiente"

    hoy = localtime().date()

    # Restricción de fecha
    try:
        fecha_str = req.GET.get('fecha', None)
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()

        # Aquí se aplica la restricción
        if fecha < hoy:
            fecha = hoy

    except:
        fecha = date(hoy.year, hoy.month, 1)

    # Límite superior: último día del mes siguiente
    fecha_max = fecha + relativedelta(months=1)
    fecha_max = date(
        fecha_max.year,
        fecha_max.month,
        calendar.monthrange(fecha_max.year, fecha_max.month)[1]
    )

    # Filtro
    if veterinario:
        citas = Cita.objects.filter(
            fecha__range=(fecha, fecha_max),
            estado=estado,
            veterinario__id=veterinario
        ).order_by('fecha')
    else:
        citas = Cita.objects.filter(
            fecha__range=(fecha, fecha_max),
            estado=estado
        ).order_by('fecha')

    veterinarios = Veterinario.objects.all().order_by('id')

    try:
        vet_loggeado = Veterinario.objects.get(usuario__id=req.user.id)
    except:
        vet_loggeado = None

    notificaciones = get_notificaciones(req)

    return render(req, 'horarios/horario.html', {
        'citas': citas,
        'fecha_min': hoy,   # Establece limite de fecha, hoy
        'fecha_max': fecha_max,
        'veterinarios': veterinarios,
        'vet_loggeado': vet_loggeado,
        'notificaciones': notificaciones
    })


@permission_required('horarios.view_notificacion', login_url="/horarios/restringido")
def ver_notificaciones(req):
    veterinario = req.GET.get('veterinario')
    if veterinario:
        veterinario = veterinario.strip()

    fecha = localtime().date()
    try:
        fecha_str = req.GET.get('fecha', None)
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        fecha_max = fecha
    except:
        fecha = date(fecha.year, fecha.month, 1)
        fecha_max = fecha + relativedelta(months=1)
        fecha_max = date(
            fecha_max.year,
            fecha_max.month,
            calendar.monthrange(fecha_max.year, fecha_max.month)[1]
        )

    try:
        notificaciones = get_notificaciones(req)
    except: 
        return redirect("restringido")

    lista_citas_notificaciones = Notificacion.objects.filter(recepcionista__usuario__id = req.user.id).values_list('cita__id', flat=True)

    if(veterinario): citas = Cita.objects.filter(fecha__range = (fecha, fecha_max), estado = "cancelado", veterinario__id = veterinario, id__in = lista_citas_notificaciones).order_by('fecha')
    else: citas = Cita.objects.filter(fecha__range = (fecha, fecha_max), estado = "cancelado", id__in = lista_citas_notificaciones).order_by('fecha')

    veterinarios = Veterinario.objects.all().order_by('id')

    return render(req, 'horarios/notificaciones.html', {
        'citas': citas,
        'fecha_min': date(2020, 1, 1),
        'fecha_max': fecha_max,
        'veterinarios': veterinarios,
        'notificaciones': notificaciones
    })

@login_required
def registrar_cita(req):
    cita_form = CitaForm()
    
    if req.method == "POST":
        cita_form = CitaForm(data=req.POST)
        print(cita_form.cleaned_data['hora_inicial'], type(cita_form.cleaned_data['hora_inicial']))
        if cita_form.is_valid():

            # Crear la cita manualmente
            cita = Cita.objects.create(
                fecha=cita_form.cleaned_data["fecha"],
                hora_inicial=int(cita_form.cleaned_data['hora_inicial']),
                veterinario=cita_form.cleaned_data["veterinario"],
                ficha_cliente=cita_form.cleaned_data["ficha_cliente"],
                estado="pendiente"
            )

            # Notificaciones por si cancelan
            if cita.estado == "cancelado":
                for recepcionista in Recepcionista.objects.all():
                    Notificacion.objects.create(
                        recepcionista=recepcionista,
                        cita=cita,
                        chequeado=False
                    )

            return redirect(reverse('registrar_cita') + '?ok')

    return render(req, 'horarios/crear_cita.html', {"form": cita_form})

@login_required
def filtrar_horas(req):
    html = "<option value="">Selecciona veterinario y fecha</option>"
    veterinario_id = req.GET.get('veterinario')
    fecha_str = req.GET.get('fecha')
    if veterinario_id == "" or fecha_str == "": return HttpResponse(html)

    fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
    dias = ['lunes', 'martes', 'miercoles', 'jueves','viernes', 'sabado','domingo']
    try:
        horario = Horario.objects.get(veterinario__id = veterinario_id)
    except:
        return HttpResponse("<option value="">No hay horario disponible</option>")
    horario_dia = getattr(horario, dias[fecha.weekday()])
    i = 1
    tiene_horario = False
    for bloque_activo in horario_dia.values():
        if i == 16: break
        print(i, bloque_activo)
        if bloque_activo:
            tiene_horario = True
            html += f"<option value='{i}'>{convertir_bloque_a_hora(i)}</option>"
        i += 1
    if not tiene_horario: return HttpResponse("<option value="">No hay horario disponible</option>")
    return HttpResponse(html)

@login_required
def vet_disponibilidad(req):
    return render(req, 'horarios/horarios.html')

@login_required
def eliminar_cita(req, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if req.user.id != cita.veterinario.usuario.id or cita.estado == "cancelado": return redirect("restringido")
    if req.method == "POST":
        cita.estado = "cancelado"
        cita.save()
        for recepcionista in Recepcionista.objects.all():
            nueva_notificacion = Notificacion.objects.create(recepcionista = recepcionista, cita = cita, chequeado = False)
            nueva_notificacion.save()
        return redirect('horarios')

    return render(req, 'horarios/eliminar_confirmacion.html', {'cita': cita})

def restringido(req):
    return render(req, 'horarios/restringido.html')

@login_required
def vet_confirmar(req):
    veterinarios = Veterinario.objects.all().order_by('id')
    if req.method == "POST":
        vet_id = req.GET.get("veterinario")
        vet = get_object_or_404(Veterinario, id= vet_id)
        return redirect(reverse("registrar_cita", f'?vet={vet.id}'))
    return render(req, 'horarios/vet_confirmar.html', {"veterinarios": veterinarios})

def convertir_bloque_a_hora(bloque):
    base = datetime(2000, 1, 1, 8, 0)
    hora = base + timedelta(minutes=(bloque - 1) * 30)
    return hora.strftime("%H:%M")
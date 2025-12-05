from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from horarios.models import Cita, Notificacion
from veterinarios.models import Recepcionista

def get_notificaciones(req):
    user_id = req.user.id
    try: recepcionista = Recepcionista.objects.get(usuario__id = user_id)
    except: recepcionista = False
    if not recepcionista:
        return 0
    notificaciones = Notificacion.objects.filter(recepcionista__id = user_id)
    return {"num": len(notificaciones), "es_recepcionista": recepcionista}

@login_required
def home(req):
    cerrar_sesion = req.GET.get('salir')
    if cerrar_sesion == "si" and req.user.is_authenticated:
        logout(req)
        redirect(reverse("home"))
    notificaciones = get_notificaciones(req)
    return render(req, "core/home.html", {"notificaciones": notificaciones})
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from horarios.models import Cita, Notificacion
from veterinarios.models import Recepcionista

def get_notificaciones(req):
    user_id = req.user.id
    recepcionista = Recepcionista.objects.get(id = user_id)
    if not recepcionista:
        return 0
    notificaciones = Notificacion.objects.filter(recepcionista__id = user_id)
    return len(notificaciones)

@login_required
def home(req):
    cerrar_sesion = req.GET.get('salir')
    if cerrar_sesion == "si" and req.user.is_authenticated:
        logout(req)
    notificaciones = get_notificaciones(req)
    return render(req, "core/home.html", {"notificaciones": notificaciones})
from django.shortcuts import render
from django.contrib.auth import logout
from horarios.models import Cita

def home(req):
    cerrar_sesion = req.GET.get('salir')
    if cerrar_sesion == "si" and req.user.is_authenticated:
        logout(req)
    citas_canceladas = Cita.objects.filter(estado = "cancelado")
    return render(req, "core/home.html", {"citas_canceladas": citas_canceladas})
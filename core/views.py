from django.shortcuts import render
from horarios.models import Cita

def home(req):
    citas_canceladas = Cita.objects.filter(estado = "cancelado")
    return render(req, "core/home.html", {"citas_canceladas": citas_canceladas})
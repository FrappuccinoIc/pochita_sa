from django.shortcuts import render

def horarios(req):
    return render(req, 'horarios/horario.html')

def vet_disponibilidad(req):
     return render(req, 'horarios/horarios.html')
from django.shortcuts import render

def perfil(req):
    return render(req, 'veterinarios/perfil.html')

def edit(req):
    return render(req, 'veterinarios/edit.html')

def horario(req):
    return render(req, 'veterinarios/horario.html')

def horario_edit(req):
    return render(req, 'veterinarios/horario_edit.html')
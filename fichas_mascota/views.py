from django.shortcuts import render

def create(req):
    return render(req, 'veterinarios/create.html')

def detalle(req):
    return render(req, 'veterinarios/detalle.html')

def edit(req):
    return render(req, 'veterinarios/edit.html')
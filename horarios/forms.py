from django import forms
from django.urls import reverse_lazy
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from .models import Cita
from django.utils.timezone import localtime
from django.conf import settings

def block_choices():
    inicio_horario = datetime(2020, 1, 1, 8, 0, 0, 0)
    resultado = []
    for i in range(16):
        hora = (inicio_horario + timedelta(minutes=30*i)).strftime("%H:%M")
        resultado.append((i+1, hora))
    return resultado

class CitaForm(forms.ModelForm):
    fecha = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(
            attrs={
                'name': "fecha",
                'class': 'form-control',
                'placeholder': 'dd/mm/aaaa',
                'autocomplete': 'off',
                "hx-get": reverse_lazy("filtrar_horas"),
                "hx-trigger": "change",
                "hx-target": "#id_hora_inicial",
                "hx-swap": "innerHTML",
                "hx-include": "[name='fecha'], [name='veterinario']"
            }
        )
    )

    hora_inicial = forms.ChoiceField(
        choices=[(None, "Selecciona veterinario y fecha")] + block_choices(), # <option value="1">08:00</option>
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Cita
        fields = "__all__"
        widgets = {
            'veterinario': forms.Select(attrs={
                'name': "veterinario",
                'class': 'form-control',
                "hx-get": reverse_lazy("filtrar_horas"),
                "hx-trigger": "change",
                "hx-target": "#id_hora_inicial",
                "hx-swap": "innerHTML",
                "hx-include": "[name='fecha'], [name='veterinario']"
            }),
            'ficha_cliente': forms.Select(attrs={'class': 'form-control'}),
        }
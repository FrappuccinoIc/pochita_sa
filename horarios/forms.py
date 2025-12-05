from django import forms
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from .models import Cita
from django.utils.timezone import localtime
from django.conf import settings

fecha_hoy = localtime().date()
fecha_max = fecha_hoy + relativedelta(months=1)
fecha_max = date(fecha_max.year, fecha_max.month, calendar.monthrange(fecha_max.year, fecha_max.month)[1])

def block_choices():
    inicio_horario = datetime(2020, 1, 1, 8, 0, 0, 0)
    resultado = []
    for i in range(16):
        hora = (inicio_horario + timedelta(minutes=30*i)).strftime("%H:%M")
        resultado.append((i+1, hora))
    return resultado

class CitaForm(forms.ModelForm):

    hora_inicial = forms.ChoiceField(choices=block_choices())
    hora_final = forms.ChoiceField(choices=block_choices())

    class Meta:
        model = Cita
        fields = "__all__"

        widgets = {
            'fecha': forms.DateInput(
                format = "%d-%m-%Y",
                attrs = {
                    'type': 'date',
                    'min': fecha_hoy,
                    'max': fecha_max
                }
            ),
            
            'hora_inicial': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 16}),
            'hora_final': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 16}),
        }
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

    fecha = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'dd/mm/aaaa',
                'autocomplete': 'off'
            }
        )
    )

    hora_inicial = forms.ChoiceField(choices=block_choices())

    """ def __init__(self, vet=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vet = vet

        if vet is not None:
            # This is just an example — replace with your vet's real unavailable hours
            

            # Filter the choices for hora_inicial
            self.fields['hora_inicial'].choices = [
                c for c in self.fields['hora_inicial'].choices
                if c[0] not in unavailable
            ] """

    class Meta:
        model = Cita
        fields = "__all__"

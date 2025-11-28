from django import forms
from datetime import datetime, timedelta
from .models import Cita
 
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
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicial': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 16}),
            'hora_final': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 16}),
        }
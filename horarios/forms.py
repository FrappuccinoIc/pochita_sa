from django import forms

from .models import Cita
 
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = "__all__"

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicial': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 16}),
            'hora_final': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 16}),
        }
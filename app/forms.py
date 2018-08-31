from django import forms
from django.contrib.auth.models import User
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fechainicio', 'horainicio', 'horafin', 'cantidadpersonas', 'user', 'insumo', 'sala']
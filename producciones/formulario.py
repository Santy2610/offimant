from django import forms
from producciones.models import producciones, materiales
from codificadores.models import centrocosto, unidadm


class formulariopro(forms.Form):
    codigo=forms.CharField()
    descripcion=forms.ModelChoiceField(queryset=centrocosto.objects.values_list('descripcion', flat=True)) # type: ignore
    unidad=forms.ModelChoiceField(queryset=unidadm.objects.values_list('unid', flat=True).order_by('unid')) # type: ignore
    cantidad=forms.FloatField()
    fechafab=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
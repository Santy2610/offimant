from django import forms
from producciones.models import producciones, materiales
from codificadores.models import centrocosto, unidadm
from vales.models import vale


class formulariopro(forms.Form):
    codigo=forms.CharField(widget=forms.TextInput(attrs={'size': '5'}))
    descripcion=forms.ModelChoiceField(queryset=centrocosto.objects.filter(prod="Si").values_list('descripcion', flat=True)) # type: ignore
    unidad=forms.ModelChoiceField(queryset=unidadm.objects.values_list('unid', flat=True).order_by('unid')) # type: ignore
    cantidad=forms.FloatField(widget=forms.TextInput(attrs={'size': '8'}))
    fechafab=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

class formulariomate(forms.Form):
    Novale=forms.ModelChoiceField(queryset=vale.objects.values_list('codigo', flat=True)) # type: ignore
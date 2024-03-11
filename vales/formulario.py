from django import forms
from codificadores.models import almacen, centrocosto, unidadm, trabajadores


class formulariovales(forms.Form):
    Codigo=forms.CharField(label="Código")
    Almacen=forms.ModelChoiceField(queryset=almacen.objects.values_list('codigo', flat=True).order_by('codigo')) # type: ignore
    Costo=forms.ModelChoiceField(queryset=centrocosto.objects.values_list('descripcion', flat=True).order_by('codigo')) # type: ignore
    Entregado=forms.ModelChoiceField(queryset=trabajadores.objects.values_list('nombre', flat=True).order_by('codigo')) # type: ignore
    Fecha=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

class formulariomaterial(forms.Form):
    Material=forms.CharField(label="Descripción")
    Unidad=forms.ModelChoiceField(queryset=unidadm.objects.values_list('unid', flat=True).order_by('unid')) # type: ignore    
    Cantidad=forms.FloatField()
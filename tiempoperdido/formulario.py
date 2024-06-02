from django import forms
from codificadores.models import areas, equipos, causas

class tiempoF(forms.Form):
    areaf=forms.ModelChoiceField(queryset=areas.objects.values_list('descripcion', flat=True).order_by('codigo'), label="Areas") # type: ignore
    equiposf=forms.ModelChoiceField(queryset=equipos.objects.values_list('descripcion', flat=True).order_by('codigo'), label="Equipos") # type: ignore
    fechaIf=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}), label="Fecha Inicio")
    fechaFf=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}), label="Fecha Final")
    causaf=forms.ModelChoiceField(queryset=causas.objects.values_list('descripcion', flat=True).order_by('codigo'), label="Causas") # type: ignore
    observacionf=forms.Textarea()
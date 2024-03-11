from django import forms

class formulariounidadm(forms.Form):
    Descripcion=forms.CharField()
    Unidad=forms.CharField()

class formularioalmacen(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField()

class formulariocosto(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField() 

class formularioareas(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField() 
       
class formularioequipos(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField()

class formulariocausas(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField()

class formulariotrab(forms.Form):
    codigo=forms.CharField()
    nombre=forms.CharField()
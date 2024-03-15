from django import forms

class formulariounidadm(forms.Form):
    Descripcion=forms.CharField(label="Descripción")
    Unidad=forms.CharField()

class formularioalmacen(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField(label="Descripción")

class formulariocosto(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField(label="Descripción") 

class formularioareas(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField(label="Descripción") 
       
class formularioequipos(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField(label="Descripción")

class formulariocausas(forms.Form):
    Codigo=forms.CharField()
    Descripcion=forms.CharField(label="Descripción")

class formulariotrab(forms.Form):
    codigo=forms.CharField()
    nombre=forms.CharField(label="Descripción")
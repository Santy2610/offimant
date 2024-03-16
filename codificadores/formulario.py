from django import forms

class formulariounidadm(forms.Form):
    Descripcion=forms.CharField(label="Descripción")
    Unidad=forms.CharField(widget=forms.TextInput(attrs={'size': '8'}))

class formularioalmacen(forms.Form):
    Codigo=forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    Descripcion=forms.CharField(label="Descripción")

class formulariocosto(forms.Form):
    Codigo=forms.CharField(widget=forms.TextInput(attrs={'size': '8'}))
    Descripcion=forms.CharField(label="Descripción") 
    obc_0 = '----'
    obc_1 = 'Si'
    obc_2 = 'No'
    prioridad = (
        (obc_0, u"----"),
        (obc_1, u"Si"),
        (obc_2, u"No"))
    Produccion=forms.ChoiceField(choices=prioridad, label="Producción")

class formularioareas(forms.Form):
    Codigo=forms.CharField(widget=forms.TextInput(attrs={'size': '5'}))
    Descripcion=forms.CharField(label="Descripción") 
       
class formularioequipos(forms.Form):
    Codigo=forms.CharField(widget=forms.TextInput(attrs={'size': '5'}))
    Descripcion=forms.CharField(label="Descripción")

class formulariocausas(forms.Form):
    Codigo=forms.CharField(widget=forms.TextInput(attrs={'size': '5'}))
    Descripcion=forms.CharField(label="Descripción")

class formulariotrab(forms.Form):
    codigo=forms.CharField(widget=forms.TextInput(attrs={'size': '5'}))
    nombre=forms.CharField(label="Descripción")
    obc_0 = '----'
    obc_1 = 'Solicita'
    obc_2 = 'Autoriza'
    prioridad = (
        (obc_0, u"----"),
        (obc_1, u"Solicita"),
        (obc_2, u"Autoriza"))
    Solic=forms.ChoiceField(choices=prioridad, label="Permisos")

    obc_0 = '----'
    obc_1 = 'Otros'
    obc_2 = 'Mantenimiento'
    prioridad = (
        (obc_0, u"----"),
        (obc_1, u"Otros"),
        (obc_2, u"Mantenimiento"))
    Person=forms.ChoiceField(choices=prioridad, label="Ubicación")
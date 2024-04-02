from django import forms
from codificadores.models import areas, equipos, trabajadores
from vales.models import vale

class fomularioorden(forms.Form):
 Codigo=forms.CharField()
 Departamento=forms.CharField()
 area=forms.ModelChoiceField(queryset=areas.objects.values_list('descripcion', flat=True).order_by('codigo')) # type: ignore
 equipo=forms.ModelChoiceField(queryset=equipos.objects.values_list('descripcion', flat=True).order_by('codigo')) # type: ignore
 idequipo=forms.CharField()
 obc_0 = '----'
 obc_1 = 'Emergencia'
 obc_2 = 'Plan de mantenimiento'
 motivos = (
        (obc_0, u"----"),
        (obc_1, u"Emergencia"),
        (obc_2, u"Plan de mantenimiento"))
 motivosolic=forms.ChoiceField(choices=motivos)
 fechaRep=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
 solicitante=forms.ModelChoiceField(queryset=trabajadores.objects.filter(person='Otros').values_list('nombre', flat=True).order_by('codigo')) # type: ignore
 obc_0 = '----'
 obc_1 = 'Si'
 obc_2 = 'No'
 afecta = (
        (obc_0, u"----"),
        (obc_1, u"Si"),
        (obc_2, u"No"))
 afectacion=forms.ChoiceField(choices=afecta)
 obc_0 = '----'
 obc_1 = 'alta'
 obc_2 = 'media'
 obc_3 = 'baja'
 prioridad = (
        (obc_0, u"----"),
        (obc_1, u"alta"),
        (obc_2, u"media"),
        (obc_3, u"baja"))
 prioridad=forms.ChoiceField(choices=prioridad)
 Resultado=forms.Textarea()
 reparado=forms.ModelChoiceField(queryset=trabajadores.objects.filter(person="Mantenimiento").values_list('nombre', flat=True).order_by('codigo')) # type: ignore
 valecod=forms.ModelChoiceField(queryset=vale.objects.values_list('codigo', flat=True).order_by('codigo'), required=False) # type: ignore
 fechaEje=forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
 obc_0 = '----'
 obc_1 = 'Uso'
 obc_2 = 'Baja técnica'
 obc_3 = 'Evaluación por control de la calidad'
 obc_4 = 'Pendiente a piezas de repuesto'
 destino = (
        (obc_0, u"----"),
        (obc_1, u"Uso"),
        (obc_2, u"Baja técnica"),
        (obc_3, u"Evaluación por control de la calidad"),
        (obc_4, u"Pendiente a piezas de repuesto"))
 Destino=forms.ChoiceField(choices=destino)

 obc_0 = '----'
 obc_1 = 'Si'
 obc_2 = 'No'
 culmina = (
        (obc_0, u"----"),
        (obc_1, u"Si"),
        (obc_2, u"No"))
 Culminada=forms.ChoiceField(choices=culmina)
 Campa=forms.CharField(required=False)

 
 
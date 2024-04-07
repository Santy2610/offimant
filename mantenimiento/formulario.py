from django import forms
from mantenimiento.models import mantplan
from codificadores.models import areas


class formmant(forms.Form):
    codigof=forms.CharField()
    areaf=forms.CharField()
    tareaf=forms.Textarea()
    enerof=forms.CheckboxInput()
    febrerof=forms.CheckboxInput()
    marzof=forms.CheckboxInput()
    abrilf=forms.CheckboxInput()
    mayof=forms.CheckboxInput()
    juniof=forms.CheckboxInput()
    juliof=forms.CheckboxInput()
    agostof=forms.CheckboxInput()
    septiembref=forms.CheckboxInput()
    octubref=forms.CheckboxInput()
    noviembref=forms.CheckboxInput()
    diciembref=forms.CheckboxInput()

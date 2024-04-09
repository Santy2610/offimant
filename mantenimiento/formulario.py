from django import forms
from mantenimiento.models import mantplan
from codificadores.models import areas


class formmant(forms.Form):
    codigof=forms.CharField(widget=forms.TextInput(attrs={'size': '5'}))
    areaf=forms.ModelChoiceField(queryset=areas.objects.values_list('descripcion', flat=True).order_by('codigo')) # type: ignore
    tareaf=forms.Textarea()
    obc_0 = ' '
    obc_1 = 'X'
    afecta = (
        (obc_0, u" "),
        (obc_1, u"X"))
    enerof=forms.ChoiceField(choices=afecta)
    enerof=forms.ChoiceField(choices=afecta)
    febrerof=forms.ChoiceField(choices=afecta)
    marzof=forms.ChoiceField(choices=afecta)
    abrilf=forms.ChoiceField(choices=afecta)
    mayof=forms.ChoiceField(choices=afecta)
    juniof=forms.ChoiceField(choices=afecta)
    juliof=forms.ChoiceField(choices=afecta)
    agostof=forms.ChoiceField(choices=afecta)
    septiembref=forms.ChoiceField(choices=afecta)
    octubref=forms.ChoiceField(choices=afecta)
    noviembref=forms.ChoiceField(choices=afecta)
    diciembref=forms.ChoiceField(choices=afecta)

from django.contrib import admin

from ordenes.models import orden
# Register your models here.

class ordenAdmin(admin.ModelAdmin):
    list_display=("codigo","area","equipo","fechaRep","prioridad","fechaEje","Resumen","Destino","valecodigo")

admin.site.register(orden, ordenAdmin)

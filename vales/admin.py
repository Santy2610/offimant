from django.contrib import admin
from vales.models import vale, materialv

# Register your models here.

class valeAdmin(admin.ModelAdmin):
    list_display=("codigo","almacen","costo","entregado","fecha")

class materialesvAdmin(admin.ModelAdmin):
    list_display=("valeID","material","unidad","cantidad")


admin.site.register(vale, valeAdmin)
admin.site.register(materialv, materialesvAdmin)    
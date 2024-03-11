from django.contrib import admin
from producciones.models import producciones, materiales

# Register your models here.

class ProduccionesAdmin(admin.ModelAdmin):
    list_display=("codigo","descripcion","unidad","cantidad")

class MaterialesAdmin(admin.ModelAdmin):
    list_display=("novale",)

admin.site.register(producciones, ProduccionesAdmin)
admin.site.register(materiales, MaterialesAdmin)         
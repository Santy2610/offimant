from django.contrib import admin

from codificadores.models import unidadm, almacen, centrocosto, areas, equipos
# Register your models here.

class unidadmAdmin(admin.ModelAdmin):
    list_display=("descripcion","unid")

class almacenAdmin(admin.ModelAdmin):
    list_display=("descripcion","codigo")    

class centrocostoAdmin(admin.ModelAdmin):
    list_display=("descripcion","codigo")

class areasAdmin(admin.ModelAdmin):
    list_display=("codigo","descripcion")

class equiposAdmin(admin.ModelAdmin):
    list_display=("masterArea", "codigo","descripcion")
 


admin.site.register(unidadm, unidadmAdmin)
admin.site.register(almacen, almacenAdmin)
admin.site.register(centrocosto, centrocostoAdmin)
admin.site.register(areas, areasAdmin)
admin.site.register(equipos, equiposAdmin)


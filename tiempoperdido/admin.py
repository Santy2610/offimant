from django.contrib import admin
from tiempoperdido.models import tiempo

# Register your models here.

class tiempoAdmin(admin.ModelAdmin):
    list_display=("area", "equipo", "fechaI", "fechaF", "causa", "observacion")

admin.site.register(tiempo, tiempoAdmin)    
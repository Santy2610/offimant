from django.contrib import admin
from mantenimiento.models import mantplan

# Register your models here.
class mantplanAdmin(admin.ModelAdmin):
    list_display=("area","tarea","eneroP","febreroP","marzoP","abrilP","mayoP","junioP","julioP","agostoP",
                 "septiembreP","octubreP","noviembreP","diciembreP","eneroR","febreroR","marzoR","abrilR","mayoR",
                 "junioR","julioR","agostoR","septiembreR","octubreR","noviembreR","diciembreR")
    
admin.site.register(mantplan, mantplanAdmin)    
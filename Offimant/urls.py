"""Offimant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Offimant.views import principal
from ordenes.views import ordenes,ordenesnew, ordenesadd, ordenesdel, ordenesupdate, ordenimpcont, ordenimpres, ordenesfilt
from codificadores.views import codunidad, codalmacen, codcosto, codparada, codunidadadd,codunidaddel 
from codificadores.views import codunidadupdate, codalmacenadd, codalmacendel,codalmacenupdate
from codificadores.views import codcostoadd, codcostodel, codcostoupdate, codareas, codareasadd
from codificadores.views import codareasdel, codareasupdate
from codificadores.views import codequipos, codequiposadd, codequiposdel, codequiposedit, codequiposupdate
from codificadores.views import codcausas, codcausasadd, codcausasdel, codcausasupdate
from codificadores.views import codtraba, codtrabaadd, codtrabadel, codtrabaupdate
from vales.views import codvales, codvalesadd, codvalesdel, codvalesupdate, codmaterial, codmaterialadd, codmaterialdel
from vales.views import codmaterialorden, consolmat, consolspe
from producciones.views import indexmate, codmateadd, codmatedel, indexprod, codproddel, codprodadd, codprodupdate
from mantenimiento.views import listmant, adicionarmant, mantadd, mantdel, mantupdate, estadomant, estadomantupdate
from tiempoperdido.views import listadotiempo, tiempodel, tiempoadd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal),
    path('consolmat', consolmat),



    path('ordenes/', ordenes),
    path('ordenesnew/<vista>/<dato>/<page>', ordenesnew),
    path('ordenesadd', ordenesadd),
    path('ordenesdel/<dato>/<page>', ordenesdel),
    path('ordenesupdate/<dato>/<page>',ordenesupdate),
    path('ordenimpcont/',ordenimpcont),
    path('ordenimpres/<dato>',ordenimpres),
    path('ordenesfilt/<dato>',ordenesfilt),



    path('codunidad/<vista>/<dato>/', codunidad),
    path('codunidadadd', codunidadadd),
    path('codunidaddel/<dato>/<page>', codunidaddel),
    path('codunidadupdate/<dato>/<page>', codunidadupdate),
    
    path('codalmacen/<vista>/<dato>/', codalmacen),
    path('codalmacenadd', codalmacenadd),
    path('codalmacendel/<dato>/<page>', codalmacendel),
    path('codalmacenupdate/<dato>/<page>', codalmacenupdate),
    
    path('codcosto/<vista>/<dato>/', codcosto),
    path('codcostoadd', codcostoadd),
    path('codcostodel/<dato>/<page>', codcostodel),
    path('codcostoupdate/<dato>/<page>', codcostoupdate),
    
    path('codareas/<vista>/<dato>/', codareas),
    path('codareasadd', codareasadd),
    path('codareasdel/<dato>/<page>', codareasdel),
    path('codareasupdate/<dato>/<page>', codareasupdate),

    path('codequipos/<dato>/', codequipos),
    path('codequiposadd/<dato>', codequiposadd),
    path('codequiposdel/<dato>/<area>/<page>', codequiposdel),
    path('codequiposedit/<dato>/<area>/', codequiposedit),
    path('codequiposupdate/<dato>/<area>/<page>', codequiposupdate),   

    path('codcausas/<vista>/<dato>/', codcausas),
    path('codcausasadd', codcausasadd),
    path('codcausasdel/<dato>/<page>', codcausasdel),
    path('codcausasupdate/<dato>/<page>', codcausasupdate),

    path('codtraba/<vista>/<dato>/', codtraba),
    path('codtrabaadd', codtrabaadd),
    path('codtrabadel/<dato>/<page>', codtrabadel),
    path('codtrabaupdate/<dato>/<page>', codtrabaupdate),
      
    path('codvales/<vista>/<dato>/', codvales),
    path('codvalesadd', codvalesadd),
    path('codvalesdel/<dato>/<page>', codvalesdel),
    path('codvalesupdate/<dato>/<page>', codvalesupdate),

    path('codmaterial/<dato>/<pagina>/', codmaterial),
    path('codmaterialadd/<dato>/<pagina>', codmaterialadd),
    path('codmaterialdel/<dato>/<vale>/<pagina>', codmaterialdel),
    path('codmaterialorden/<dato>/<page>/<retro>/', codmaterialorden),
    path('consolmat', consolmat),
    path('consolspe/<dato>', consolspe),

 
    path('codparada', codparada),

    path('indexprod/<vista>/<dato>/', indexprod),
    path('codprodadd', codprodadd),
    path('codproddel/<dato>/<page>', codproddel),
    path('codprodupdate/<dato>/<page>', codprodupdate),

    path('indexmate/<dato>/<pagina>', indexmate),
    path('codmateadd/<dato>/<pagina>', codmateadd),
    path('codmatedel/<dato>/<ubica>/<pagina>', codmatedel),

    path('listmant', listmant),
    path('adicionarmant/<vista>/<dato>/<page>', adicionarmant),
    path('mantadd', mantadd), 
    path('mantdel/<dato>', mantdel),
    path('mantupdate/<dato>/<page>', mantupdate),     
    path('estadomant/<dato>/<page>', estadomant),
    path('estadomantupdate/<dato>/<page>', estadomantupdate),


    path('listadotiempo', listadotiempo),
    path('tiempodel/<dato>', tiempodel),
    path('tiempoadd', tiempoadd),

]

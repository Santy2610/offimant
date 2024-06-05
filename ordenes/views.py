from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ordenes.models import orden
from ordenes.formulario import fomularioorden
from django.db.models import Sum, Count

def ordenes(request):
     page=request.GET.get('page',1)
     ordenlist=orden.objects.all().order_by('codigo')
     paginador=Paginator(ordenlist, 10)
     ordenlist=paginador.page(page)
     dato="SED"
     return render(request,"listadoordenes.html",{"ordensw":ordenlist, "paginador":paginador,"listpsw":ordenlist, "datosw":dato})

def ordenesfilt(request, dato):
     page=request.GET.get('page',1)
     ordenlist=orden.objects.filter(area=dato).order_by('codigo')
     paginador=Paginator(ordenlist, 10)
     ordenlist=paginador.page(page)
     return render(request,"listadoordenes.html",{"ordensw":ordenlist, "paginador":paginador,"listpsw":ordenlist, "datosw":dato})     

def ordenesnew(request, vista, dato, page):
      if vista == 'index':
       dept=orden.objects.values('departamento').order_by('departamento').annotate(contador=Count('departamento'))
       formorden=fomularioorden()
       return render(request,"adicionarordenes.html",{"form":formorden, "vistasw":vista, "datosw":dato, "deptsw":dept})
      else:
       ordenubica=orden.objects.get(pk=dato)
       formorden=fomularioorden(initial={'Codigo':ordenubica.codigo,'area':ordenubica.area,'equipo':ordenubica.equipo,
       'fechaRep':ordenubica.fechaRep,'prioridad':ordenubica.prioridad,'fechaEje':ordenubica.fechaEje,'Destino':ordenubica.Destino,
       'valecod':ordenubica.valecodigo, 'Departamento':ordenubica.departamento, 'idequipo':ordenubica.idequipo,
       'motivosolic':ordenubica.motivosolic, 'solicitante':ordenubica.solicitante, 'afectacion':ordenubica.Afectacion,
       'prioridad':ordenubica.prioridad, 'reparado':ordenubica.Reparado, 'Destino':ordenubica.Destino,'Culminada':ordenubica.culminada,
       'Campa':ordenubica.campa})
       result=ordenubica.Resumen
       falla=ordenubica.falla
       clog=orden.objects.values('departamento').order_by('departamento').annotate(contador=Count('departamento'))      
       return render(request,"adicionarordenes.html",{"form":formorden, "resultsw":result,"fallasw":falla, "vistasw":vista, "datosw":dato, "pagesw":page, "clogsw":clog})

def ordenesadd(request):
     Codigof=request.GET["Codigo"]
     Departamentof=request.GET["Departamento"]
     areaf=request.GET["area"]
     equipof=request.GET["equipo"]
     idequipof=request.GET["idequipo"]
     fechaRepf=request.GET["fechaRep"]
     motivosolicf=request.GET["motivosolic"]
     fallaf=request.GET["Falla"]
     solicitantef=request.GET["solicitante"]
     afectacionf=request.GET["afectacion"]
     prioridadf=request.GET["prioridad"]
     Resultadof=request.GET["Resultado"]
     reparadof=request.GET["reparado"]
     valef=request.GET["valecod"]
     fechaejef=request.GET["fechaEje"]
     destinof=request.GET["Destino"]
     culminadaf=request.GET["Culminada"]
     campa=request.GET["Campa"]
     ordenlist=orden.objects.create(codigo=Codigof, departamento=Departamentof, area=areaf,
                                      equipo=equipof, idequipo=idequipof, fechaRep=fechaRepf,
                                      motivosolic=motivosolicf, falla=fallaf, solicitante=solicitantef,
                                      Afectacion=afectacionf, prioridad=prioridadf, Resumen=Resultadof,
                                      Reparado=reparadof,valecodigo=valef, Destino=destinof, fechaEje=fechaejef,
                                      culminada=culminadaf, campa=campa)
     return redirect(ordenes)

def ordenesupdate(request, dato, page):
     Codigof=request.GET["Codigo"]
     Departamentof=request.GET["Departamento"]
     areaf=request.GET["area"]
     equipof=request.GET["equipo"]
     idequipof=request.GET["idequipo"]
     fechaRepf=request.GET["fechaRep"]
     motivosolicf=request.GET["motivosolic"]
     fallaf=request.GET["Falla"]
     solicitantef=request.GET["solicitante"]
     afectacionf=request.GET["afectacion"]
     prioridadf=request.GET["prioridad"]
     Resultadof=request.GET["Resultado"]
     reparadof=request.GET["reparado"]
     valef=request.GET["valecod"]
     Destinof=request.GET["Destino"]
     fechaejef=request.GET["fechaEje"]
     culminadaf=request.GET["Culminada"]
     campa=request.GET["Campa"]
     ordenlist=orden.objects.get(pk=dato)
     ordenlist.codigo=Codigof
     ordenlist.departamento=Departamentof
     ordenlist.area=areaf
     ordenlist.equipo=equipof
     ordenlist.idequipo=idequipof
     ordenlist.fechaRep=fechaRepf
     ordenlist.motivosolic=motivosolicf
     ordenlist.falla=fallaf
     ordenlist.solicitante=solicitantef
     ordenlist.Afectacion=afectacionf
     ordenlist.prioridad=prioridadf
     ordenlist.fechaEje=fechaejef
     ordenlist.Resumen=Resultadof
     ordenlist.Reparado=reparadof
     ordenlist.Destino=Destinof
     ordenlist.valecodigo=valef
     ordenlist.culminada=culminadaf
     ordenlist.campa=campa
     ordenlist.save()
     return redirect("/ordenes/?page=%s" %page)

def ordenesdel(request, dato):
     ordenlist=orden.objects.get(pk=dato)
     ordenlist.delete()
     return redirect(ordenes)

def ordenimpcont(request):
     ordenimp=orden.objects.all().order_by('codigo')
     return render(request,"indexcontrol.html", {"ordensw":ordenimp})

def ordenimpres(request, dato):
     ordenimp=orden.objects.get(pk=dato)
     return render(request,"OrdenImpres.html",{"ordensw":ordenimp})


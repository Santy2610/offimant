from django.shortcuts import render
from Offimant.views import barracont, tareaM, tiempoP

# Create your views here.


def indexsys(request):
    return render(request, "indexsys.html", {"contadorSW": barracont(), "ordenmSW": tareaM(), 'tiempopSW': tiempoP()})

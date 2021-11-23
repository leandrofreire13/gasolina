from django.shortcuts import render

# Create your views here.
from gastos.models import Gasto


def listaGastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'index.html', {'gastos': gastos})

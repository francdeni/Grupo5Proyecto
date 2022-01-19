from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import Context
from django.template import loader
import datetime

# Create your views here.

def inicio(request):
    return render(request, "AppGrupo5/inicio.html")

def instrumentos(request):
    return render(request, "AppGrupo5/instrumento.html")

def pedal(request):
    return render(request, "AppGrupo5/pedal.html")

def disco(request):
    return render(request, "AppGrupo5/disco.html")
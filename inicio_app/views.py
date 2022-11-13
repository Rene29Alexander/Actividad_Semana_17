from django.shortcuts import render
from django.template import context



# Create your views here.

def menu(request):
    return render(request,'menu_principal.html',{"username":"Usuario"})

def about(request):
    return render(request,'about.html')

def prueba(request):
    return render(request,'prueba.html')

def formulario(request):
    return render(request, "formulario.html", {"grado1":"Primero",
    "grado2":"Segundo","grado3":"Tercero","grado4":"Cuarto","grado5":"Quinto",
    "grado6":"Secto","grado7":"Septimo","grado8":"Octavo","grado9":"Noveno",})

def servicios(request):
    return render(request,'servicios.html')

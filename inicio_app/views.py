from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm




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


def registro(request):
    form = UserCreationForm()

    if request.method=="post":
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()
    context = {"form":form}
    

    return render(request,'register.html', context) 

def clientescrud(request):
    listaAlumno = Alumno.objects.all()
    return render(request,'clientescrud.html', {"alumno":listaAlumno})

def addalumno(request):
    nombre=request.POST['inputnombre']
    docente=request.POST['inputdocente']
    edad=request.POST['inputedad']
    codigo_estudiantes=request.POST['inputcodigo']
    seccion=request.POST['inputseccion']

    alumno= Alumno.objects.create(
        nombre=nombre, docente=docente, edad=edad, codigo_estudiantes=codigo_estudiantes, seccion=seccion
    )
    return redirect('/clientes') 


def editcliente(request,id):
    alumno=Alumno.objects.get(id=id)
    return render(request,'editcliente.html', {"alumno":alumno})

def guardarcliente(request,id): 
    nombre=request.POST['inputnombre']
    docente=request.POST['inputdocente']
    edad=request.POST['inputedad']
    codigo_estudiantes=request.POST['inputcodigo']
    seccion=request.POST['inputseccion']

    id=Alumno.objects.get(id=id)
    id.nombre=nombre
    id.docente=docente
    id.edad=edad
    id.codigo_estudiantes=codigo_estudiantes
    id.seccion=seccion
    id.save()
    return redirect('/clientes')     

def delcliente(request,id):
    alumno=Alumno.objects.get(id=id)
    alumno.delete()      
    return redirect('/clientes')  




def materiascrud(request):
    listaMaterias = Materia.objects.all()
    return render(request,'materiacrud.html', {"materia":listaMaterias})

def addmateria(request):
    codigo=request.POST['inputcodigo']
    nombre=request.POST['inputnombre']
    descripcion=request.POST['inputdescripcion']

    materia= Materia.objects.create(
        codigo=codigo, nombre=nombre, descripcion=descripcion
    )
    return redirect('/materias') 

def editmateria(request,id):
    materia=Materia.objects.get(id=id)
    return render(request,'editmateria.html', {"materia":materia})

def guardarmateria(request,id): 
    codigo=request.POST['inputcodigo']
    nombre=request.POST['inputnombre']
    descripcion=request.POST['inputdescripcion']

    id=Materia.objects.get(id=id)
    id.codigo=codigo
    id.nombre=nombre
    id.descripcion=descripcion
    id.save()
    return redirect('/materias')     

def delmateria(request,id):
    materia=Materia.objects.get(id=id)
    materia.delete()      
    return redirect('/materias')





def seccioncrud(request):
    listaseccion = Secciones.objects.all()
    return render(request,'seccioncrud.html', {"seccion":listaseccion})

def addseccion(request):
    seccion=request.POST['inputseccion']
    codigo=request.POST['inputcodigo']
    descripcion=request.POST['inputdescripcion']
    ubicacion=request.POST['inputubicacion']

    seccion= Secciones.objects.create(
        seccion=seccion, codigo=codigo, descripcion=descripcion, ubicacion=ubicacion
    )
    return redirect('/seccion')

def editseccion(request,id):
    seccion=Secciones.objects.get(id=id)
    return render(request,'editseccion.html', {"seccion":seccion})

def guardarseccion(request,id): 
    seccion=request.POST['inputseccion']
    codigo=request.POST['inputcodigo']
    descripcion=request.POST['inputdescripcion']
    ubicacion=request.POST['inputubicacion']

    id=Secciones.objects.get(id=id)
    id.seccion=seccion
    id.codigo=codigo
    id.descripcion=descripcion
    id.ubicacion=ubicacion
    id.save()
    return redirect('/seccion')     

def delseccion(request,id):
    seccion=Secciones.objects.get(id=id)
    seccion.delete()      
    return redirect('/seccion')



def docentecrud(request):
    listadocente = Docente.objects.all()
    return render(request,'docentecrud.html', {"docente":listadocente})

def adddedocente(request):
    nombre=request.POST['inputnombre']
    edad=request.POST['inputedad']
    grado=request.POST['inputgrado']
    seccion=request.POST['inputseccion']
    numero_alumno=request.POST['inputnumero']
    Materia=request.POST['inputmateria']
    

    docente= Docente.objects.create(
        nombre=nombre, edad=edad, grado=grado, seccion=seccion, numero_alumno=numero_alumno, Materia=Materia,
    )
    return redirect('/docente')


def editdocente(request,id):
    docente=Docente.objects.get(id=id)
    return render(request,'editdocente.html', {"docente":docente})

def guardardocente(request,id): 
    nombre=request.POST['inputnombre']
    edad=request.POST['inputedad']
    grado=request.POST['inputgrado']
    seccion=request.POST['inputseccion']
    numero_alumno=request.POST['inputnumero']
    Materia=request.POST['inputmateria']

    id=Docente.objects.get(id=id)
    id.nombre=nombre
    id.edad=edad
    id.grado=grado
    id.seccion=seccion
    id.numero_alumno=numero_alumno
    id.Materia=Materia
    id.save()
    return redirect('/docente')

def deldocente(request,id):
    docente=Docente.objects.get(id=id)
    docente.delete()      
    return redirect('/docente') 


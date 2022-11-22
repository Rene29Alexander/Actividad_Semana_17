from django.db import models

# Create your models here.

class Materia(models.Model):
    codigo=models.CharField(max_length=200, null=True)
    nombre=models.CharField(max_length=200, null=True)
    descripcion=models.TextField()
    

class Secciones(models.Model):
    seccion=models.CharField(max_length=200, null=True)
    codigo=models.CharField(max_length=200, null=True)
    descripcion=models.TextField()
    ubicacion=models.TextField()
   


class Docente(models.Model):
    nombre=models.CharField(max_length=200, null=True)
    edad=models.IntegerField(default='0')
    grado=models.CharField(max_length=200, null=True)
    seccion=models.CharField(max_length=2, null=True)
    numero_alumno=models.IntegerField(default=0)
    Materia = models.CharField(max_length=200, null=True)

    


    
class Alumno(models.Model):
    nombre=models.CharField(max_length=200, null=True)
    edad=models.IntegerField(default='0')
    docente=models.CharField(max_length=200, null=True)
    codigo_estudiantes=models.CharField(max_length=20)
    seccion=models.CharField(max_length=1, null=True)







    
from django.db import models

# Create your models here.

class Materia(models.Model):
    codigo=models.CharField(max_length=200, null=True)
    nombre=models.CharField(max_length=200, null=True)
    descripcion=models.TextField()
    def __str__(self):
        return str(self.nombre)

class Secciones(models.Model):
    seccion=models.CharField(max_length=200, null=True)
    codigo=models.CharField(max_length=200, null=True)
    descripcion=models.TextField()
    ubicacion=models.TextField()
    def __str__(self):
        return str(self.seccion)


class Docente(models.Model):
    nombre=models.CharField(max_length=200, null=True)
    edad=models.IntegerField(default='0')
    grado=models.CharField(max_length=200, null=True)
    seccion=models.ForeignKey(Secciones, on_delete=models.CASCADE)
    numero_alumno=models.IntegerField(default=0)
    Materia = models.ForeignKey(Materia,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)


    
class Alumno(models.Model):
    nombre=models.CharField(max_length=200, null=True)
    edad=models.IntegerField(default='0')
    Docente=models.ForeignKey(Docente, on_delete=models.CASCADE)
    codigo_estudiantes=models.CharField(max_length=10)
    seccion=models.ForeignKey(Secciones, on_delete=models.CASCADE)







    
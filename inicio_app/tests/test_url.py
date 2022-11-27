from django.test import SimpleTestCase
from django.urls import reverse, resolve
from inicio_app.views import*

class Testurls(SimpleTestCase):

    def test_url(self):
      url= reverse('principal')
      print(resolve(url))
      self.assertEquals(resolve(url).func,menu)

      url= reverse('acercade')
      print(resolve(url))
      self.assertEquals(resolve(url).func,about)

      url= reverse('form')
      print(resolve(url))
      self.assertEquals(resolve(url).func,formulario)

      url= reverse('servicio')
      print(resolve(url))
      self.assertEquals(resolve(url).func,servicios)

      url= reverse('registro')
      print(resolve(url))
      self.assertEquals(resolve(url).func,registro)

      url= reverse('login')
      print(resolve(url))
      self.assertEquals(resolve(url).func,vistalogin)

      url= reverse('cerrarsesion')
      print(resolve(url))
      self.assertEquals(resolve(url).func,cerrarsesion)

      url= reverse('adminclientes')
      print(resolve(url))
      self.assertEquals(resolve(url).func,clientescrud)

      url= reverse('admincliente')
      print(resolve(url))
      self.assertEquals(resolve(url).func,addalumno)

      url= reverse('adminMaterias')
      print(resolve(url))
      self.assertEquals(resolve(url).func,materiascrud)

      url= reverse('adminMateria')
      print(resolve(url))
      self.assertEquals(resolve(url).func,addmateria)

      url= reverse('adminSeccions')
      print(resolve(url))
      self.assertEquals(resolve(url).func,seccioncrud)

      url= reverse('adminSeccion')
      print(resolve(url))
      self.assertEquals(resolve(url).func,addseccion)

      url= reverse('adminDocentes')
      print(resolve(url))
      self.assertEquals(resolve(url).func,docentecrud)

      url= reverse('adminDocente')
      print(resolve(url))
      self.assertEquals(resolve(url).func,adddedocente)

      









      


      

      
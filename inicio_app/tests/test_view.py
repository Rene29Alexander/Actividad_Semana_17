from django.test import TestCase, Client
from django.urls import reverse
from inicio_app.models import *

class TestViews(TestCase):

    def test_view(self):
        client = Client()
        response = client.get(reverse('principal'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'menu_principal.html')

        client = Client()
        response = client.get(reverse('acercade'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'about.html')

        client = Client()
        response = client.get(reverse('form'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'formulario.html')

        client = Client()
        response = client.get(reverse('servicio'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'servicios.html')

        client = Client()
        response = client.get(reverse('adminclientes'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'clientescrud.html')

        client = Client()
        response = client.get(reverse('adminMaterias'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'materiacrud.html')

        client = Client()
        response = client.get(reverse('adminSeccions'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'seccioncrud.html')

        client = Client()
        response = client.get(reverse('adminDocentes'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'docentecrud.html')






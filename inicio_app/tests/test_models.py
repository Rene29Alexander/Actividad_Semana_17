from django.test import TestCase
from inicio_app.models import *

class TestModels(TestCase):

    def test_model(self):
        self.Materiaprueba = Materia.objects.create(
            codigo=123456,
            nombre="Ciencias",
            descripcion="Materia me ciencias"
        )

        self.Seccioneprueba = Secciones.objects.create(
            seccion="A",
            codigo="secccion_001",
            descripcion="Seccion nunero 1",
            ubicacion="Primera planta, primer salon"
        )

        self.Docenteprueba = Docente.objects.create(
            nombre="Julia",
            edad=21,
            grado="primero",
            seccion="B",
            numero_alumno=21,
            Materia="Lenguaje"
        )

        self.Alumnoprueba = Alumno.objects.create(
            nombre="Matias",
            edad=9,
            docente="Julia",
            codigo_estudiantes="SMIS060720",
            seccion="A"
        )

from django.urls import path
from .views import *




urlpatterns = [
    
    path('menu/', menu, name="principal"),
    path('about/', about,name="acercade"),
    path('',prueba,),
    path('forn/',formulario,name="form"),
    path('servicios/',servicios,name="servicio"),
    path('registro/', registro,name="registro"),


    path('clientes/',clientescrud,name="adminclientes"),
    path('addalumno/', addalumno, name="admincliente"),
    path('delclientes/<id>', delcliente, name="delclientes"),
    path('editcliente/<id>', editcliente, name="editcliente"),
    path('guardarcliente/<id>', guardarcliente, name="guardarcliente"),



    path('materias/', materiascrud, name="adminMaterias"),
    path('addmateria/', addmateria, name="adminMateria"),
    path('delmateria/<id>', delmateria, name="delmateria"),
    path('editmateria/<id>', editmateria, name="editmateria"),
    path('guardarmateria/<id>', guardarmateria, name="guardarmateria"),


    path('seccion/', seccioncrud, name="adminSeccions"),
    path('addseccion/', addseccion, name="adminSeccion"),
    path('delseccion/<id>', delseccion, name="delseccion"),
    path('editseccion/<id>', editseccion, name="editseccion"),
    path('guardarseccion/<id>', guardarseccion, name="guardarseccion"),

    
    path('docente/', docentecrud, name="adminDocentes"),
    path('adddocente/', adddedocente, name="adminDocente"),
    path('deldocentes/<id>', deldocente, name="deldocentes"),
    path('editdocente/<id>', editdocente, name="editdocente"),
    path('guardardocente/<id>', guardardocente, name="guardardocente"),

   
    
    

]
from django.urls import path
from .views import *


urlpatterns = [
    
    path('menu/', menu, name="principal"),
    path('about/', about,name="acercade"),
    path('',prueba,),
    path('forn/',formulario,name="form"),
    path('servicios/',servicios,name="servicio"),
    

]
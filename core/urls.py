from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # dirección para el administrador.
    path('admin/', admin.site.urls),
    
    # dirección de la vista principal -> la que se ve primero.
    path('',views.index, name='principal'),
    
    # dirección de un saludo.
    path('saludo/',views.saludo, name='saludo'),
    
    # dirección de un saludo mejorado ingresando una variable.
    path('saludoMejorado/<str:nombre>', views.saludoMejorado, name='saludo2'),
    
    # dirección para la vista contacto.
    path('contacto/',views.contacto, name='contacto'),
    
    # dirección para la vista sobreNosotros con un parámetro por la URL.
    path('sobreNosotros/<str:nombre>',views.sobreNosotros, name='sobreNosotros')
]

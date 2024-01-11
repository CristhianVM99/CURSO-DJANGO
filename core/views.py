from django.http import HttpResponse
from django.shortcuts import render

# TODO: retorna una respuesta por defecto.
def index(request):
    return HttpResponse("Hola Mundo")

# TODO: retorna un saludo.
def saludo(request):
    return HttpResponse("Hola saludos desde Django")

# TODO: retorna un saludo con un nombre personalizado.
def saludoMejorado(request, nombre):
    return HttpResponse(f"Hola {nombre} como estas?")

# TODO: retorna una vista html 
def contacto(request):
    return render(request,'contacto.html',{})

# TODO: retorna una vista html con una variables adicional para el contexto.
def sobreNosotros(request,nombre):
    lenguajes = ['php','java','c','c#','c++','python','js','go','rust','ruby','kotlin']
    context = { 'nombre' : nombre, 'lenguajes' : lenguajes }
    return render(request,'sobreNosotros.html',context)
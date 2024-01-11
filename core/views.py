from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo")

def saludo(request):
    return HttpResponse("Hola saludos desde Django")
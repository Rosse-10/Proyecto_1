from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>¡Felicidades! Mi primera página en Django funciona.</h1>")
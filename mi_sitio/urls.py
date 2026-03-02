from django.contrib import admin
from django.urls import path
from inicio.views import hola_mundo  # <-- Cambia 'hola' por 'hola_mundo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola_mundo),  # <-- Aquí también cámbialo a 'hola_mundo'
]
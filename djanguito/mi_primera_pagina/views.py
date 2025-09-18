from django.shortcuts import render
from django.http import HttpResponse

# Vista original
def index(request):
    return HttpResponse("Hello, World!")

# Vista con operación matemática (ejemplo: suma)
def suma(request):
    a = 5
    b = 7
    resultado = a + b
    return HttpResponse(f"La suma de {a} + {b} es = {resultado}")

# Vista que renderiza un HTML
def saludo_html(request):
    contexto = {
        "nombre": "Omar",
        "mensaje": "Bienvenido a tu primera página en Django 🚀"
    }
    return render(request, "saludo.html", contexto)

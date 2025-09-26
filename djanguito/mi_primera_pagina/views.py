from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index (request):
    return render(request, "mi_primera_pagina/index.html")

def about (request):
    return render(request, "mi_primera_pagina/about.html")

def saludo (request, nombre):
    return render(request, "mi_primera_pagina/saludo.html",
                  {"nombre": nombre.capitalize()})

def suma (request, a, b):
    return render(request, "mi_primera_pagina/suma.html",
                  {"a": a, "b": b, "resultado": a + b})
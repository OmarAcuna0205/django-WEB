from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Task
tasks = ["foo", "bar", "baz"]

def index (request):
    return render(request, "mi_primera_pagina/index.html")

def about (request):
    return render(request, "mi_primera_pagina/about.html")

def saludo (request, nombre):
    return render(request, "mi_primera_pagina/saludo.html", {
        "nombre": nombre.capitalize()
    })

def suma (request, a, b):
    resultado_suma = int(a) + int(b)
    return render(request, "mi_primera_pagina/suma.html", {
        "a": a, 
        "b": b, 
        "resultado": resultado_suma
    })

def tasks_index (request):
    tasks = Task.objects.all() 
    return render(request, "mi_primera_pagina/tasks_index.html", {
        "tasks": tasks
    })

def tasks_add(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            tasks.append(task) 
        return HttpResponseRedirect(reverse("tasks_index"))
    return render(request, "mi_primera_pagina/tasks_add.html")

def tasks_admin_list (request):
    tasks = Task.objects.all().order_by("created_at")
    return render(request, "mi_primera_pagina/tasks_admin_list.html", {
        "tasks": tasks
    })

def index2 (request): 
    return render(request, "mi_primera_pagina/index2.html")
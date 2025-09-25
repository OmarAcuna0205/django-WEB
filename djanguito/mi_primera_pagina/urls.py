from django.urls import path
from . import views

# urlpatterns para la aplicación 'mi_primera_pagina'
urlpatterns = [
    # 1. La página de inicio ahora es la raíz del sitio ('')
    path('', views.index, name='index'),

    # 2. Rutas limpias y directas para las otras páginas
    path('about/', views.about, name='about'),
    path('suma/<int:a>/<int:b>/', views.suma, name='suma'),
    
    # 3. Se hizo la ruta 'saludo' más específica para evitar conflictos
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
]
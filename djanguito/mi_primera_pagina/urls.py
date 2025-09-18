from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              # Hello, World!
    path('suma/', views.suma, name='suma'),           # Operación matemática
    path('saludo/', views.saludo_html, name='saludo') # Renderiza HTML
]
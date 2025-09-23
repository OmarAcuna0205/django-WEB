from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),             
    path('suma/', views.suma, name='suma'),           
    path('saludo/', views.saludo_html, name='saludohtml'), 
    path('<str:nombre>', views.saludo, name='saludo'),
]
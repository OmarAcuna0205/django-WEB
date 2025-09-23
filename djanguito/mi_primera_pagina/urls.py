from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),             
    path('suma/', views.suma, name='suma'),           
    path('saludo/', views.saludo_html, name='saludohtml'), 
    path('<str:nombre>', views.saludo, name='saludo'),
    path('index/', views.index, name='index'),
]
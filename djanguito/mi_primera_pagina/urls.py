from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),             
    path('index/about/', views.about, name='about'),
    path('index/suma/<int:a>/<int:b>/', views.suma, name='suma'),
    path('<str:nombre>/', views.saludo, name='saludo'),
]
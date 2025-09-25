from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('suma/<int:a>/<int:b>/', views.suma, name='suma'),
    
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
]
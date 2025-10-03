from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('suma/<int:a>/<int:b>/', views.suma, name='suma'),
    
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),

    path('tasks/menu/', views.index2, name='index2'),
    path('tasks/list/', views.tasks_index, name='tasks_index'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/admin/', views.tasks_admin_list, name='tasks_admin_list'),
]
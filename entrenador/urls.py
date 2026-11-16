
from django.urls import path
from . import views

app_name = 'entrenador'

urlpatterns = [
    path('', views.lista_entrenadores, name='lista_entrenadores'),
    path('crear/', views.crear_entrenador, name='crear_entrenador'),
    path('editar/<int:id_entrenador>/', views.editar_entrenador, name='editar_entrenador'),
    path('eliminar/<int:id_entrenador>/', views.eliminar_entrenador, name='eliminar_entrenador'),
]

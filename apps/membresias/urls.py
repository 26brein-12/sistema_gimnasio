
from django.urls import path
from . import views

app_name = 'membresias'

urlpatterns = [
    path('', views.lista_membresias, name='lista_membresias'),
    path('crear/', views.crear_membresia, name='crear_membresia'),
    path('editar/<int:id_membresia>/', views.editar_membresia, name='editar_membresia'),
    path('eliminar/<int:id_membresia>/', views.eliminar_membresia, name ='eliminar_membresia'),
]

from django.urls import path
from . import views

app_name = 'inscripcion'

urlpatterns = [
    path('', views.lista_inscripciones, name='lista_inscripciones'),
    path('crear/', views.crear_inscripcion, name='crear_inscripcion'),
    path('editar/<int:id_inscripcion>/', views.editar_inscripcion, name='editar_inscripcion'),
    path('eliminar/<int:id_inscripcion>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]
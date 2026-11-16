from django.urls import path
from . import views

app_name = 'clase'

urlpatterns = [
    path('', views.lista_clases, name='lista_clases'),
    path('crear/', views.crear_clase, name='crear_clase'),
    path('editar/<int:id_clase>/', views.editar_clase, name='editar_clase'),
    path('eliminar/<int:id_clase>/', views.eliminar_clase, name='eliminar_clase'),
]
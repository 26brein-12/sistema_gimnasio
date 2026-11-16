
from django.urls import path
from . import views
app_name = 'socios'
urlpatterns = [
    path('', views.lista_socios, name='lista_socios'),
    path('crear/', views.crear_socio, name='crear_socio'),
    path('editar/<int:id_socio>/', views.editar_socio, name='editar_socio'),
    path('eliminar/<int:id_socio>/', views.eliminar_socio, name='eliminar_socio'),
]

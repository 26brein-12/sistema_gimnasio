from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.lista_planes, name='lista_planes'),
    path('crear/', views.crear_plan, name='crear_plan'),
    path('editar/<int:id_plan>/', views.editar_plan, name='editar_plan'),
    path('eliminar/<int:id_plan>/', views.eliminar_plan, name='eliminar_plan'),
]
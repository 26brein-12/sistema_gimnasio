from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('socios/', include('socios.urls')),
    path('membresias/', include('membresias.urls')),
    path('planes/', include('plan.urls')),
    path('entrenadores/', include('entrenador.urls')),
    path('clases/', include('clase.urls')),
    path('inscripciones/', include('inscripcion.urls')),
]

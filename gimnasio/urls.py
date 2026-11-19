from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('socios/', include('apps.socios.urls')),
    path('membresias/', include('apps.membresias.urls')),
    path('planes/', include('apps.plan.urls')),
    path('entrenadores/', include('apps.entrenador.urls')),
    path('clases/', include('apps.clase.urls')),
    path('inscripciones/', include('apps.inscripcion.urls')),
]

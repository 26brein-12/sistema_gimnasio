from django.contrib import admin
from .models import Clase

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id_clase',  'horario', 'nombre', 'cupo', 'entrenador')
    search_fields = ('horario', 'descripcion','entrenador_nombre')
    list_filter = ('horario','entrenador')
from django.contrib import admin
from .models import entrenador

@admin.register(entrenador)
class entrenadorAdmin(admin.ModelAdmin):
    list_display = ('id_entrenador', 'documento', 'nombre', 'telefono', 'especialidad', 'activo')
    search_fields = ('documento', 'documento', 'nombre', 'especialidad')
    list_filter = ('activo','especialidad')

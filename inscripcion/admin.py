from django.contrib import admin
from .models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'socio','clase', 'fecha_inscripcion')
    search_fields = ('socio_nombres', 'socio_apellidos', 'socio_documento', 'clase_nombre')
    list_filter = ('fecha_inscripcion','clase')

from django.contrib import admin
from .models import Socio

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('id_socio', 'documento', 'nombres', 'apellidos', 'telefono', 'correo', 'activo')
    search_fields = ('documento', 'nombres', 'apellidos', 'correo')
    list_filter = ('activo',)

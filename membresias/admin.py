from django.contrib import admin
from .models import Membresia

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('id_membresia', 'socio', 'plan', 'fecha_inicio', 'fecha_fin', 'activa',)
    search_fields = ('socio_nombres', 'socio_apellidos', 'socio_documento', 'plan_nombre_plan',)
    list_filter = ('activa','fecha_inicio','fecha_fin', 'plan',)

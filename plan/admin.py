from django.contrib import admin
from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):

    list_display = ('id_plan', 'nombre_plan','precio', 'duracion_dias', 'activo',)
    search_fields = ('nombre_plan', 'descripcion',)
    list_filter = ('activo',)


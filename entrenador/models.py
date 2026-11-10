from django.db import models

class entrenador(models.Model):
    id_entrenador = models.AutoField(primary_key=True)
    documento  = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    def __str__ (self):
        return f"{self.id_entrenador} - {self.nombre}"


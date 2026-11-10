from django.db import models
from entrenador.models import entrenador


class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    horario = models.DateTimeField()
    cupo = models.PositiveIntegerField()
    entrenador = models.ForeignKey(entrenador, on_delete=models.CASCADE )

    def __str__(self):
        return self.nombre



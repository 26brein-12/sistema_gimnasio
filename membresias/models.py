
from django.db import models
from socios.models import Socio
from plan.models import Plan


class Membresia(models.Model):
    id_membresia = models.AutoField(primary_key=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"Membresía {self.id_membresia} - {self.socio}"


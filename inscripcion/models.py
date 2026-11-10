from django.db import models
from socios.models import Socio
from clase.models import Clase


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.socio} - {self.clase}"

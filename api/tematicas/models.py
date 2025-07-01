from django.db import models
from api.tipos_eventos.models import TiposDeEventos

class Tematicas(models.Model):
    nombre_tematica = models.CharField(max_length=20, unique=True)
    descripcion_tematica = models.TextField()
    tipo_tematica = models.ForeignKey(TiposDeEventos, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'tematicas'

# estado: funcional
# Create your models here.

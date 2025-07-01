from django.db import models
from api.tematicas.models import Tematicas
class FechasEventos(models.Model):
    fecha_evento = models.DateTimeField(auto_now_add=True)
    evento =  models.ForeignKey(Tematicas, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'fechasEventos'

# estado: con fallas

# estado: corregido, funcional
# Create your models here.

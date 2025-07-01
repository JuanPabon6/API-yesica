from django.db import models
from api.ventas.models import Ventas

class DetallesVentas(models.Model):
    fecha_venta = models.DateField(auto_now_add=True)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'detalles_ventas'

# estado: funcional
# Create your models here.

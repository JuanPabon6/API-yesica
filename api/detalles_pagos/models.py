from django.db import models
from api.ventas.models import Ventas
from api.pagos.models import Pagos

class DetallesPagos(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, default=1)
    pago = models.ForeignKey(Pagos, on_delete=models.CASCADE, default=1)

# estado: funcional
# Create your models here.

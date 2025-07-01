from django.db import models
from api.clientes.models import Clientes
from api.empleados.models import Empleados

class Ventas(models.Model):
    fecha_venta = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, default=1)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'ventas'

# estado: funcional
# Create your models here.

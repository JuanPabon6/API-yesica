from django.db import models
from api.clientes.models import Clientes
from api.tipos_eventos.models import TiposDeEventos
from api.tematicas.models import Tematicas
from api.fechas_eventos.models import FechasEventos
from api.materiales.models import Materiales
from api.detalles_pagos.models import DetallesPagos
from api.empleados.models import Empleados


class FacturasDeClientes(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, default=1)
    tipo_evento = models.ForeignKey(TiposDeEventos, on_delete=models.CASCADE, default=1)
    tematica = models.ForeignKey(Tematicas, on_delete=models.CASCADE, default=1)
    materiales = models.ForeignKey(Materiales, on_delete=models.CASCADE, default=1)
    fecha_evento = models.ForeignKey(FechasEventos, on_delete=models.CASCADE, default=1)
    empleado_factura = models.ForeignKey(Empleados, on_delete=models.CASCADE, default=1)
    detalle_pago = models.ForeignKey(DetallesPagos, on_delete=models.CASCADE, default=1)
    total = models.IntegerField()

    class Meta:
        db_table = 'facturasDeClientes'

# estado: funcional
# Create your models here.

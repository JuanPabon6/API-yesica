from django.db import models

class FormasPagos(models.Model):
    metodo_pago = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'formas_pagos'

# estado: funcional
# Create your models here.

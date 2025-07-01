from django.db import models
from api.materiales.models import Materiales

class Compras(models.Model):
    fecha_compra = models.DateField(auto_now_add=True)
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField()
    

    class Meta:
        db_table = 'compras'

# estado: funcional
# Create your models here.

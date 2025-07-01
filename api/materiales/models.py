from django.db import models

class Materiales(models.Model):
    material = models.CharField(max_length=30)
    precio = models.FloatField()
    marca = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'materiales'

# estado: funcional
# Create your models here.

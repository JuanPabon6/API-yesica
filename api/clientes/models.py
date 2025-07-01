from django.db import models

class Clientes(models.Model):
    Identificacion = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=30)
    Apellidos = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=15, unique=True)
    Direccion = models.CharField(max_length=40)
    Ciudad = models.CharField(max_length=15)
    Email = models.EmailField(max_length=40, unique=True)
    Fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'

# estado: funcional
# Create your models here.

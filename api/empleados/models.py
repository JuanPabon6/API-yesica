from django.db import models

class Empleados(models.Model):
    Identificacion = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=20)
    Telefono = models.CharField(max_length=15, unique=True)
    Email = models.EmailField(max_length=40)
    contraseña = models.CharField(max_length=15,unique=True, null=False)

    class Meta:
        db_table = 'empleados'

# estado: funcional
# Create your models here.

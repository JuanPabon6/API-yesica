from django.db import models

class TiposDeEventos(models.Model):
    tipo_evento = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    class Meta:
        db_table = 'tipos_eventos'

# estado: funcional
# Create your models here.

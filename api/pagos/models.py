from django.db import models
from api.formas_pago.models import FormasPagos

class Pagos(models.Model):
    fecha_pago = models.DateField(auto_now_add=True)
    forma_pago= models.ForeignKey(FormasPagos, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'pagos'

# estado: funcional
# Create your models here.

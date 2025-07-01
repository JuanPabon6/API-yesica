from rest_framework import serializers
from .models import FacturasDeClientes

class FacturasDeClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = FacturasDeClientes
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
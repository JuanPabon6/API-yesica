from rest_framework import serializers
from .models import DetallesPagos

class DetallesPagosSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetallesPagos
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
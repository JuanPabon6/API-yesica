from rest_framework import serializers
from .models import DetallesVentas

class DetallesVentasSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetallesVentas
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
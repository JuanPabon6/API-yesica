from rest_framework import serializers
from .models import Ventas

class VentasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        extra_kwargs ={
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
            }
        fields = '__all__'
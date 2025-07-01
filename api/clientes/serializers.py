from rest_framework import serializers
from .models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
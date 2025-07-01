from rest_framework import serializers
from .models import Empleados

class EmpleadosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
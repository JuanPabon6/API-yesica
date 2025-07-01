from rest_framework import serializers
from .models import FormasPagos

class FormasPagosSerializers(serializers.ModelSerializer):
    class Meta:
        model = FormasPagos
        extra_kwargs ={
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
from rest_framework import serializers
from .models import Compras

class ComprasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Compras
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
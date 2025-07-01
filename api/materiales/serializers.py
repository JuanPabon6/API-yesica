from rest_framework import serializers
from .models import Materiales

class MaterialesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Materiales
        extra_kwargs ={
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
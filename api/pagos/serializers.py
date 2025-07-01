from rest_framework import serializers
from .models import Pagos

class PagosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
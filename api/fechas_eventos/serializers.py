from rest_framework import serializers
from .models import FechasEventos

class FechasEventosSerializers(serializers.ModelSerializer):
    class Meta:
        model = FechasEventos
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
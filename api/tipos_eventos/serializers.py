from rest_framework import serializers
from .models import TiposDeEventos

class TiposDeEventosSerializers(serializers.ModelSerializer):
    class Meta:
        model = TiposDeEventos
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
from rest_framework import serializers
from .models import Tematicas


class TematicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tematicas
        extra_kwargs = {
            'created_at':{'read_only':True},
            'updated_at':{'read_only':True}
        }
        fields = '__all__'
        
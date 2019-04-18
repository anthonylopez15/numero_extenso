from rest_framework.serializers import ModelSerializer

from core.models import Numero


class NumeroSerializer(ModelSerializer):
    class Meta:
        model = Numero
        fields = '__all__'

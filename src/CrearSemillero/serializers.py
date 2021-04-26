from rest_framework import serializers
from .models import CrearSemillero


class CrearSemilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrearSemillero
        fields = '__all__'

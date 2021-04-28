from rest_framework import serializers
from .models import InscribirseASemillero


class InscribirseASemilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscribirseASemillero
        fields = '__all__'

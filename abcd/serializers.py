
from rest_framework import serializers
from .models import GameNumber, Sign


class GameNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameNumber
        fields = '__all__'

class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = '__all__'


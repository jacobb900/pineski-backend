from rest_framework import serializers
from .models import Pin, PinImage

class PinImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PinImage
        fields = ['id', 'image']

class PinSerializer(serializers.ModelSerializer):
    # 'images' musi pasować do 'related_name' w modelu PinImage
    images = PinImageSerializer(many=True, read_only=True)

    class Meta:
        model = Pin
        fields = [
            'id',
            'name',
            'description',
            'address',
            'latitude',
            'longitude',
            'category',
            'images', # To pole teraz przesyła tablicę obiektów ze zdjęciami
            'created_at'
        ]
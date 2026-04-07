from rest_framework import serializers
from .models import Pin, PinImage


class PinImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PinImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url if obj.image else None


class PinSerializer(serializers.ModelSerializer):
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
            'mount_date',
            'direction',
            'images',
            'created_at',
        ]
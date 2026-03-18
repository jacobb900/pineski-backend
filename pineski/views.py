from rest_framework import viewsets
from .models import Pin
from .serializers import PinSerializer
class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
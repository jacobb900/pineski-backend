from rest_framework import viewsets, permissions
from .models import Pin
from .serializers import PinSerializer

class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer

    def get_permissions(self):
        # 'list' (widok listy) i 'retrieve' (pojedynczy pin) - pozwól każdemu (nawet niezalogowanym)
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        # Każda inna akcja (dodawanie, usuwanie, edycja) - tylko dla zalogowanych adminów
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
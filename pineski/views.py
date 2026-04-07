from rest_framework import viewsets, permissions
from .models import Pin, PinImage
from .serializers import PinSerializer


class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # 1. Zapisujemy podstawowe dane pineski
        pin = serializer.save()

        # 2. Wyciągamy listę plików z klucza 'uploaded_images'
        # (musi być zgodny z tym, co wysyła React w FormData)
        images = self.request.FILES.getlist('uploaded_images')

        # 3. Tworzymy obiekty PinImage dla każdego zdjęcia
        for image in images:
            PinImage.objects.create(pin=pin, image=image)

    def perform_update(self, serializer):
        # 1. Aktualizujemy dane pineski
        pin = serializer.save()

        # 2. Opcjonalnie: jeśli przesyłasz nowe zdjęcia przy edycji
        images = self.request.FILES.getlist('uploaded_images')
        if images:
            # Jeśli chcesz nadpisać starą galerię, odkomentuj linię poniżej:
            # pin.images.all().delete()
            for image in images:
                PinImage.objects.create(pin=pin, image=image)
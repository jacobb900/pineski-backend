from django.db import models


class Pin(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Kategoria (dodaję ją tutaj, bo na froncie już ją mamy w kodzie)
    category = models.CharField(max_length=50, default='food')

    # Możesz zostawić to pole jako 'miniaturkę' lub usunąć po migracji
    image = models.ImageField(upload_to='pin_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.address}"


# --- TO JEST NOWA CZĘŚĆ DLA GALERII ---
class PinImage(models.Model):
    # powiązanie z Pin: jeden Pin może mieć wiele PinImage
    pin = models.ForeignKey(Pin, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pin_gallery/')

    def __str__(self):
        return f"Zdjęcie do: {self.pin.name}"
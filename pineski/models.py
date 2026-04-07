from django.db import models


DIRECTION_CHOICES = [
    ('N',  'Północ (N)'),
    ('NE', 'Północny-wschód (NE)'),
    ('E',  'Wschód (E)'),
    ('SE', 'Południowy-wschód (SE)'),
    ('S',  'Południe (S)'),
    ('SW', 'Południowy-zachód (SW)'),
    ('W',  'Zachód (W)'),
    ('NW', 'Północny-zachód (NW)'),
]


class Pin(models.Model):
    name        = models.CharField(max_length=255, verbose_name='Nazwa')
    description = models.TextField(blank=True, null=True, verbose_name='Opis historyczny')
    address     = models.CharField(max_length=255, blank=True, default='', verbose_name='Adres')
    latitude    = models.FloatField(verbose_name='Szerokość geograficzna')
    longitude   = models.FloatField(verbose_name='Długość geograficzna')
    category    = models.CharField(max_length=50, default='food', verbose_name='Kategoria')
    image       = models.ImageField(upload_to='pin_images/', blank=True, null=True)

    # --- NOWE POLA ---
    mount_date  = models.DateField(blank=True, null=True, verbose_name='Data montażu puszki')
    direction   = models.CharField(
        max_length=3, blank=True, default='',
        choices=DIRECTION_CHOICES,
        verbose_name='Kierunek świata',
    )

    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Puszka'
        verbose_name_plural = 'Puszki'

    def __str__(self):
        return f"{self.name} ({self.address})"


class PinImage(models.Model):
    pin   = models.ForeignKey(Pin, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pin_gallery/')

    class Meta:
        verbose_name = 'Zdjęcie puszki'
        verbose_name_plural = 'Zdjęcia puszek'

    def __str__(self):
        return f"Zdjęcie → {self.pin.name}"
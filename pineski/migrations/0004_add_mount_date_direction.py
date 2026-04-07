from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pineski', '0003_add_category_description_pinimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='mount_date',
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name='Data montażu puszki',
            ),
        ),
        migrations.AddField(
            model_name='pin',
            name='direction',
            field=models.CharField(
                max_length=3,
                blank=True,
                default='',
                verbose_name='Kierunek świata (N/NE/E/SE/S/SW/W/NW)',
                choices=[
                    ('N',  'Północ (N)'),
                    ('NE', 'Północny-wschód (NE)'),
                    ('E',  'Wschód (E)'),
                    ('SE', 'Południowy-wschód (SE)'),
                    ('S',  'Południe (S)'),
                    ('SW', 'Południowy-zachód (SW)'),
                    ('W',  'Zachód (W)'),
                    ('NW', 'Północny-zachód (NW)'),
                ],
            ),
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pineski', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]

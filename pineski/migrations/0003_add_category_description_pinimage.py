from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pineski', '0002_fix_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pin',
            name='category',
            field=models.CharField(default='food', max_length=50),
        ),
        migrations.AddField(
            model_name='pin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pin_images/'),
        ),
        migrations.CreateModel(
            name='PinImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pin_gallery/')),
                ('pin', models.ForeignKey(on_delete=models.CASCADE, related_name='images', to='pineski.pin')),
            ],
        ),
    ]

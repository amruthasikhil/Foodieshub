# Generated by Django 5.1.4 on 2025-02-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='pimg',
            field=models.ImageField(blank=True, null=True, upload_to='Cart_image'),
        ),
    ]

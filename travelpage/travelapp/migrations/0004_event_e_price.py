# Generated by Django 5.0.5 on 2024-05-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_event_e_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='e_price',
            field=models.FloatField(default='0'),
        ),
    ]

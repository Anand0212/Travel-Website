# Generated by Django 5.0.6 on 2024-06-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0022_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirm',
            name='amt',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

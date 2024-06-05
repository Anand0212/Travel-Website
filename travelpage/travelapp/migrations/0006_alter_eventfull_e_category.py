# Generated by Django 5.0.5 on 2024-05-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_eventfull_alter_event_e_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventfull',
            name='e_category',
            field=models.IntegerField(choices=[(1, 'Day Trek'), (2, 'Camping'), (3, 'Family Tour'), (4, 'Backpacking')], verbose_name='category'),
        ),
    ]
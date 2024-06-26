# Generated by Django 5.0.5 on 2024-05-17 06:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0009_eventfull_e_itinerary'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('c_name', models.CharField(max_length=30)),
                ('c_phone', models.BigIntegerField()),
                ('pid', models.ForeignKey(db_column='p_id', on_delete=django.db.models.deletion.CASCADE, to='travelapp.eventfull')),
                ('userid', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='EventDetails',
        ),
    ]

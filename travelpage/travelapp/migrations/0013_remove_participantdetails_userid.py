# Generated by Django 5.0.5 on 2024-05-17 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0012_remove_enroll_c_name_remove_enroll_c_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantdetails',
            name='userid',
        ),
    ]

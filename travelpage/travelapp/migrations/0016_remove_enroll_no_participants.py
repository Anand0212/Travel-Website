# Generated by Django 5.0.5 on 2024-05-18 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0015_delete_participantdetails_remove_enroll_eid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='no_participants',
        ),
    ]

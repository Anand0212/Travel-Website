# Generated by Django 5.0.5 on 2024-05-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0014_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParticipantDetails',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='eid',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='userid',
        ),
        migrations.AddField(
            model_name='enroll',
            name='c_mobile',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enroll',
            name='c_name',
            field=models.CharField(default='anand', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enroll',
            name='no_participants',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

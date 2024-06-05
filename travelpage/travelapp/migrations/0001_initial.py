# Generated by Django 5.0.5 on 2024-05-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=50)),
                ('e_category', models.CharField(max_length=50)),
                ('e_desc', models.CharField(max_length=300)),
                ('e_date', models.DateField()),
            ],
        ),
    ]

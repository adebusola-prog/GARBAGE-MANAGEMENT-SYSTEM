# Generated by Django 4.2 on 2023-05-06 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("garbage_app", "0003_location_address"),
    ]

    operations = [
        migrations.RemoveField(model_name="collectionplan", name="frequency",),
    ]

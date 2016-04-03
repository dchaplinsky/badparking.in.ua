# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 22:15
from __future__ import unicode_literals

from django.db import migrations


def populate_types(apps, schema_editor):
    crime_type_model = apps.get_model("core", "CrimeType")
    crime_type_model(
        name="Паркування на перехресті",
        enabled=True).save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_types)
    ]

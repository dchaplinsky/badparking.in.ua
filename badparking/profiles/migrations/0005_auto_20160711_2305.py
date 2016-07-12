# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20160528_0007'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', profiles.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.AddField(
            model_name='user',
            name='external_id',
            field=models.CharField(blank=True, db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='provider_type',
            field=models.CharField(blank=True, choices=[('privat_bankid', 'Privatbank BankID'), ('oschad_bankid', 'Oschadbank BankID'), ('facebook', 'Facebook')], db_index=True, max_length=255),
        ),
    ]

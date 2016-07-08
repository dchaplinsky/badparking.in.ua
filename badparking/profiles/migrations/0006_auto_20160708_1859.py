# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 15:59
from __future__ import unicode_literals

from django.db import migrations


def update_usernames(apps, schema_editor):
    User = apps.get_model('profiles', 'User')
    for user in User.objects.filter(is_staff=False):
        user.username = 'inn_{}'.format(user.username)
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20160708_1859'),
    ]

    operations = [
        migrations.RunPython(update_usernames, migrations.RunPython.noop)
    ]

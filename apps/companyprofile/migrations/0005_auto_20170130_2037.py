# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-30 19:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0004_auto_20160413_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('name',), 'permissions': (('view_company', 'View Company'),), 'verbose_name': 'Bedrift', 'verbose_name_plural': 'Bedrifter'},
        ),
        migrations.RemoveField(
            model_name='company',
            name='old_image',
        ),
    ]

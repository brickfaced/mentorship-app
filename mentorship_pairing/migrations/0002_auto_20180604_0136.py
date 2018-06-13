# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship_profile', '0002_auto_20180113_0519'),
        ('mentorship_pairing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='pairing',
            managers=[
                ('active_pairings', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='pairing',
            name='requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_pairing', to='mentorship_profile.Profile'),
        ),
        migrations.AlterField(
            model_name='pairing',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('discontinued', 'Discontinued')], default='pending', max_length=40),
        ),
    ]

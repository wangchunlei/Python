# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=1, max_length=20, verbose_name='\u5bc6\u7801'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='code',
            field=models.CharField(max_length=200, verbose_name='\u5e10\u53f7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='fingerprint',
            field=models.ImageField(upload_to=b'', verbose_name='\u6307\u7eb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='logintype',
            field=models.CharField(max_length=1, verbose_name='\u7c7b\u578b', choices=[(0, b'Form'), (1, b'FingerPrint')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_code',
            field=models.CharField(max_length=200, verbose_name='\u7f16\u7801'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=200, verbose_name='\u540d\u79f0'),
            preserve_default=True,
        ),
    ]

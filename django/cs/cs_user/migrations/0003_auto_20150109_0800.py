# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_user', '0002_auto_20150109_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='fingerprint',
            field=models.ImageField(upload_to=b'', verbose_name='\u6307\u7eb9', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='logintype',
            field=models.CharField(max_length=1, verbose_name='\u7c7b\u578b', choices=[(b'0', b'Form'), (b'1', b'FingerPrint')]),
            preserve_default=True,
        ),
    ]

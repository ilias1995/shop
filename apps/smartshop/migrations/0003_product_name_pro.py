# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartshop', '0002_auto_20141126_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_pro',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]

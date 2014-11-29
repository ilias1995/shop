# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='nameproduct',
            field=models.ForeignKey(default=2, to='smartshop.NameProduct'),
            preserve_default=False,
        ),
    ]

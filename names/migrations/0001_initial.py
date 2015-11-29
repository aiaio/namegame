# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name.', max_length=100)),
                ('used', models.BooleanField(default=False, help_text=b'Check after the name is used.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

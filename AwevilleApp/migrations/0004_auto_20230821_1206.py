# Generated by Django 3.2.7 on 2023-08-21 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AwevilleApp', '0003_auto_20230821_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='CheckIn',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 12, 6, 1, 135676)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='CheckOut',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 3.2.7 on 2023-08-24 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AwevilleApp', '0010_auto_20230824_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='RoomTitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='CheckIn',
            field=models.CharField(default=datetime.datetime(2023, 8, 24, 12, 55, 35, 961286), max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 12, 55, 35, 961286), editable=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 12, 55, 35, 962285), editable=False),
        ),
    ]

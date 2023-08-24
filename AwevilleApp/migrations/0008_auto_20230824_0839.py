# Generated by Django 3.2.7 on 2023-08-24 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AwevilleApp', '0007_auto_20230824_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='CheckIn',
            field=models.CharField(default=datetime.datetime(2023, 8, 24, 8, 39, 22, 883577), max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='DateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 8, 39, 22, 883577), editable=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='DatePub',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 8, 39, 22, 884579), editable=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='Image',
            field=models.ImageField(upload_to='upload'),
        ),
    ]

# Generated by Django 2.0.4 on 2019-04-23 10:01

from django.db import migrations
import separatedvaluesfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20190423_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devrequest',
            name='developers',
            field=separatedvaluesfield.models.SeparatedValuesField(max_length=150, null=True),
        ),
    ]

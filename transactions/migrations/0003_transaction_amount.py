# Generated by Django 2.0.4 on 2018-10-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20181008_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]

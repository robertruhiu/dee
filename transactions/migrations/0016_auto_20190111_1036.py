# Generated by Django 2.0.4 on 2019-01-11 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_auto_20190111_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.OpenCall'),
        ),
    ]
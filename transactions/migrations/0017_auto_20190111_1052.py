# Generated by Django 2.0.4 on 2019-01-11 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0016_auto_20190111_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Transaction'),
        ),
    ]
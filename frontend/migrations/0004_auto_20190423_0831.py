# Generated by Django 2.0.4 on 2019-04-23 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_newuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='candidate',
        ),
        migrations.DeleteModel(
            name='Newuser',
        ),
    ]

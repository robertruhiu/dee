# Generated by Django 2.0.4 on 2019-04-16 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
    ]

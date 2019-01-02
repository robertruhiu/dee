# Generated by Django 2.0.1 on 2018-01-18 18:07

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('classroom', 'Subject')
    Subject.objects.create(name='React js', image='https://i.ibb.co/ZNvW1j9/react.png')
    Subject.objects.create(name='Express js', image='https://i.ibb.co/w7PbkNy/expressjslogo-1.png')
    Subject.objects.create(name='Laravel', image='https://i.ibb.co/QF95CBt/laravel.png')
    Subject.objects.create(name='Django', image='https://i.ibb.co/QNBHFRJ/django.png')
    Subject.objects.create(name='Angular', image='https://i.ibb.co/sj9zhLz/angular.png')
    Subject.objects.create(name='Angularjs', image='https://i.ibb.co/sj9zhLz/angular.png')
    Subject.objects.create(name='Rubyonrails', image='https://i.ibb.co/t2KgQY1/rails.png')
    Subject.objects.create(name='Nodejs', image='https://i.ibb.co/YhSJDNw/node.png')
    Subject.objects.create(name='Vue', image='https://i.ibb.co/0yjKGjC/vue.png')
    Subject.objects.create(name='Javascript', image='https://i.ibb.co/dPbdXXr/javascript.png')
    Subject.objects.create(name='Python', image='https://i.ibb.co/WFv6Y09/python.png')
    Subject.objects.create(name='Java', image='https://i.ibb.co/wMwjgqw/java.png')
    Subject.objects.create(name='Sql', image='https://i.ibb.co/H724NDW/sql.png')
    Subject.objects.create(name='C++', image='https://i.ibb.co/hFrDjkf/c.png')
    Subject.objects.create(name='C#', image='https://i.ibb.co/44RtSgj/c.png')
    Subject.objects.create(name='Php', image='https://i.ibb.co/18R20M7/php.png')
    Subject.objects.create(name='Ruby', image='https://i.ibb.co/mTB8yKB/ruby.png')
    Subject.objects.create(name='Android', image='https://i.ibb.co/WswfGVg/android.png')


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
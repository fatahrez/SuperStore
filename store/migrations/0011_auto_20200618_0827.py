# Generated by Django 3.0.7 on 2020-06-18 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200618_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clerk',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='clerk',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='last_name',
        ),
    ]
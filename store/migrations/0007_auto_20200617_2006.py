# Generated by Django 3.0.7 on 2020-06-17 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200617_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbatch',
            name='clerk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Clerk'),
        ),
    ]

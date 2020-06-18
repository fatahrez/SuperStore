# Generated by Django 3.0.7 on 2020-06-17 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200617_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbatch',
            name='clerk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Clerk'),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Item'),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Supplier'),
        ),
    ]

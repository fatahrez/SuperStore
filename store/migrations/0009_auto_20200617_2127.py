# Generated by Django 3.0.7 on 2020-06-17 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200617_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbatch',
            name='clerk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Clerk'),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Item'),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Supplier'),
        ),
    ]

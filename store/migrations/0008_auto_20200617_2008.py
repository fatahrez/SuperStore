# Generated by Django 3.0.7 on 2020-06-17 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200617_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbatch',
            name='clerk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Clerk'),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Item'),
        ),
        migrations.AlterField(
            model_name='productbatch',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.Supplier'),
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-10 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0003_auto_20211110_2134'),
        ('product', '0002_product_supplier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myuser.supplier'),
        ),
    ]
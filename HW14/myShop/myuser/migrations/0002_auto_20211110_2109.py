# Generated by Django 3.2.9 on 2021-11-10 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.customer'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.customer'),
        ),
    ]
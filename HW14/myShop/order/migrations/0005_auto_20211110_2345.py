# Generated by Django 3.2.9 on 2021-11-10 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0004_alter_comment_customer'),
        ('product', '0003_auto_20211110_2134'),
        ('order', '0004_emailtosupplier_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.customer'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
    ]

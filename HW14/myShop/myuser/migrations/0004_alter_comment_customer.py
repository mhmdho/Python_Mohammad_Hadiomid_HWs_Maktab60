# Generated by Django 3.2.9 on 2021-11-10 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0003_auto_20211110_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.customer'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

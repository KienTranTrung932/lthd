# Generated by Django 3.2.5 on 2021-10-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_sanpham_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='mota',
            field=models.TextField(max_length=255),
        ),
    ]

# Generated by Django 3.2.5 on 2021-10-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_auto_20211015_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='hinhanh',
            field=models.ImageField(default=None, upload_to='sanpham/%Y/%m'),
        ),
    ]

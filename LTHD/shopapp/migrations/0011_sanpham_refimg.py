# Generated by Django 3.2.5 on 2021-11-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0010_alter_sanpham_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='refimg',
            field=models.ImageField(default=None, upload_to='sanpham/%Y/%m'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.5 on 2021-11-06 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0011_sanpham_refimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sanpham',
            old_name='refimg',
            new_name='hinhanh',
        ),
    ]

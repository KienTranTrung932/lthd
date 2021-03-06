# Generated by Django 3.2.5 on 2021-11-13 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0012_rename_refimg_sanpham_hinhanh'),
    ]

    operations = [
        migrations.CreateModel(
            name='SanPhamThuocDonHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluong', models.CharField(default=1, max_length=255)),
                ('donhang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.donhang')),
                ('sanpham', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopapp.sanpham')),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2021-02-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enoch', '0002_auto_20201020_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SPC', 'SPC'), ('WPC', 'WPC'), ('Rockwood Board', 'Rockwood Board'), ('HDF Board with accessories', 'HDF Board with accessories'), ('Others', 'Others')], default=('SPC', 'SPC'), max_length=200),
        ),
    ]

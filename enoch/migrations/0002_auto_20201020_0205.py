# Generated by Django 3.0.8 on 2020-10-19 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enoch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SPC', 'SPC'), ('WPC', 'WPC'), ('Rockwood Board', 'Rockwood Board'), ('Toilet Partition', 'Toilet Partition'), ('Others', 'Others')], default=('SPC', 'SPC'), max_length=200),
        ),
    ]

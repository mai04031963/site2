# Generated by Django 4.2 on 2023-07-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_demands_аппарат_demands_серийный_номер_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demands',
            name='Адрес',
            field=models.CharField(blank=True, max_length=80, verbose_name='Адрес'),
        ),
    ]

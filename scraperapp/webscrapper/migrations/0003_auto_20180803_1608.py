# Generated by Django 2.0.7 on 2018-08-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapper', '0002_auto_20180803_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='hero_image',
            field=models.ImageField(upload_to='webscrapper/imgs/'),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='picture',
            field=models.ImageField(upload_to='webscrapper/imgs/author'),
        ),
    ]
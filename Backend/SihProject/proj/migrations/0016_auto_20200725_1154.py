# Generated by Django 3.0.6 on 2020-07-25 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0015_auto_20200724_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeimages',
            name='ngoName',
        ),
        migrations.RemoveField(
            model_name='activeimages',
            name='reviewed',
        ),
    ]
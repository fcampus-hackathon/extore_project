# Generated by Django 2.1 on 2019-06-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20190628_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
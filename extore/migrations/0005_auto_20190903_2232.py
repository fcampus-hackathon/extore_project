# Generated by Django 2.1 on 2019-09-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extore', '0004_invitedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=15),
        ),
    ]

# Generated by Django 2.1 on 2019-09-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20190903_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
# Generated by Django 2.1 on 2019-09-05 15:48

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True),
        ),
    ]

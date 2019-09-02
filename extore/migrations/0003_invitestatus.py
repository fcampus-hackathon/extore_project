# Generated by Django 2.1 on 2019-08-18 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extore', '0002_auto_20190818_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.ManyToManyField(blank=True, related_name='accepted', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='extore.Group')),
                ('invited', models.ManyToManyField(blank=True, related_name='invited', to=settings.AUTH_USER_MODEL)),
                ('rejected', models.ManyToManyField(blank=True, related_name='rejected', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.1 on 2019-08-18 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, default='', max_length=120, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='group_images/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_groups', to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(blank=True, related_name='members_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
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

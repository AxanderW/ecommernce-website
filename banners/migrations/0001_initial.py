# Generated by Django 3.0.3 on 2020-09-21 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'bannercategory',
                'verbose_name_plural': 'bannercategories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='BannerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='banneritem')),
                ('text1', models.TextField(blank=True, default='', null=True)),
                ('text2', models.TextField(blank=True, default='', null=True)),
                ('text3', models.TextField(blank=True, default='', null=True)),
                ('text4', models.TextField(blank=True, default='', null=True)),
                ('text5', models.TextField(blank=True, default='', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('bannercategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='banners.BannerCategory')),
            ],
            options={
                'verbose_name': 'banneritem',
                'verbose_name_plural': 'banneritems',
                'ordering': ('name',),
            },
        ),
    ]

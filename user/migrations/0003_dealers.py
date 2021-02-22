# Generated by Django 3.1.2 on 2020-11-06 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=225, null=True)),
                ('dealer_phone', models.CharField(max_length=225, null=True)),
                ('dealer_address', models.CharField(max_length=225, null=True)),
                ('dealer_website', models.CharField(max_length=225, null=True)),
                ('shop_image', models.ImageField(blank=True, max_length=10000, null=True, upload_to='')),
                ('shop_name', models.CharField(max_length=225, null=True)),
                ('shop_number', models.CharField(max_length=225, null=True)),
                ('shop_location', models.CharField(max_length=225, null=True)),
                ('shop_place', models.CharField(max_length=225, null=True)),
                ('shop_opening_time', models.TimeField(max_length=225, null=True)),
                ('shop_closing_time', models.TimeField(max_length=225, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.0.2 on 2020-11-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0028_auto_20201121_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='reff_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='refferd_user',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

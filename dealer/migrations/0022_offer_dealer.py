# Generated by Django 2.0.2 on 2020-11-19 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_catogeries'),
        ('dealer', '0021_auto_20201119_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ad.Dealers'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_reffreal_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reffreal_offer',
            name='reff_discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reffreal_offer',
            name='refferd_person_discount',
            field=models.IntegerField(null=True),
        ),
    ]

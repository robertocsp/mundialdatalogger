# Generated by Django 2.2.6 on 2020-01-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20191023_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperatura',
            name='degelo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='temperatura',
            name='temperatura',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

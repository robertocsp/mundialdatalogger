# Generated by Django 2.2.6 on 2019-10-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191022_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuito',
            name='conformidade',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='core.Conformidade'),
        ),
    ]
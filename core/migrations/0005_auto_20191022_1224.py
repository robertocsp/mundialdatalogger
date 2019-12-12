# Generated by Django 2.2.6 on 2019-10-22 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_circuito_posicao_coluna'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conformidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='temperatura',
            name='degelo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='circuito',
            name='conformidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Conformidade'),
        ),
    ]

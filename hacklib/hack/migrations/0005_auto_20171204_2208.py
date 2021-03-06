# Generated by Django 2.0 on 2017-12-04 22:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0004_auto_20171204_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('estado', models.CharField(choices=[('RV', 'En revision'), ('RJ', 'rechazado'), ('AC', 'Aceptado')], default='RV', max_length=2)),
                ('puntos', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_cre',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 22, 8, 28, 77109, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='articulo',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hack.Usuario'),
        ),
    ]

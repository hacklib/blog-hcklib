# Generated by Django 2.0 on 2017-12-04 19:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Rango',
            new_name='rango',
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_cre',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 19, 46, 18, 474486, tzinfo=utc)),
        ),
    ]
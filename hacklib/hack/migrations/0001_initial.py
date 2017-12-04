# Generated by Django 2.0 on 2017-12-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=250)),
                ('Rango', models.CharField(choices=[('NB', 'Noob'), ('AD', 'Administrador'), ('LM', 'Lammer'), ('TL', 'Troll'), ('MD', 'Medio'), ('EX', 'Experto'), ('MS', 'Maestro'), ('CR', 'Creador')], default='NB', max_length=2)),
            ],
        ),
    ]

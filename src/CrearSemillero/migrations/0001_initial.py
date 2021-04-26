# Generated by Django 3.2 on 2021-04-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearSemillero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeSemillero', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('fechaInicio', models.DateTimeField(auto_now_add=True)),
                ('fechaFin', models.DateTimeField(auto_now_add=True)),
                ('hora', models.CharField(max_length=20)),
                ('linkReunion', models.CharField(max_length=200)),
            ],
        ),
    ]

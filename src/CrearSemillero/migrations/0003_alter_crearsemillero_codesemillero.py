# Generated by Django 3.2 on 2021-04-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrearSemillero', '0002_auto_20210425_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearsemillero',
            name='codeSemillero',
            field=models.IntegerField(),
        ),
    ]
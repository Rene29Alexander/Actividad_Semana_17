# Generated by Django 4.1.2 on 2022-11-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_app', '0003_alter_docente_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='codigo_estudiantes',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-05 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200, null=True)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Secciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=200, null=True)),
                ('codigo', models.CharField(max_length=200, null=True)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('edad', models.IntegerField(max_length=0)),
                ('grado', models.CharField(max_length=200, null=True)),
                ('seccion', models.CharField(max_length=200, null=True)),
                ('numero_alumno', models.IntegerField(default=0)),
                ('Materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio_app.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('edad', models.IntegerField(default=0)),
                ('codigo_estudiantes', models.CharField(max_length=3)),
                ('Docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio_app.docente')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio_app.secciones')),
            ],
        ),
    ]

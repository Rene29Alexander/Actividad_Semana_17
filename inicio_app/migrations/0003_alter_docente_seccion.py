# Generated by Django 4.1.2 on 2022-11-05 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio_app', '0002_alter_alumno_edad_alter_docente_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio_app.secciones'),
        ),
    ]
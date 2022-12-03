# Generated by Django 4.1 on 2022-09-20 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=20, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=20, verbose_name='Apellido Materno')),
                ('nombres', models.CharField(max_length=20, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha De Nacimiento')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'db_table': 'docente',
                'ordering': ['apellido_paterno', '-apellido_materno'],
            },
        ),
        migrations.AddField(
            model_name='cursos',
            name='Docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Academia.docente'),
        ),
    ]

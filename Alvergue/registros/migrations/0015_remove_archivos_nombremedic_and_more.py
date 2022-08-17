# Generated by Django 4.0.5 on 2022-07-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0014_medicamentos_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivos',
            name='NombreMedic',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='fechaCad',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='status',
        ),
        migrations.RemoveField(
            model_name='archivos',
            name='stock',
        ),
        migrations.AddField(
            model_name='archivos',
            name='CURP',
            field=models.CharField(max_length=100, null=True, verbose_name='CURP'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='Direccion',
            field=models.CharField(max_length=100, null=True, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='Edad',
            field=models.IntegerField(null=True, verbose_name='Edad'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='Medicamento',
            field=models.CharField(max_length=100, null=True, verbose_name='Medicamentos a Tomar'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='NombrePaciente',
            field=models.CharField(max_length=150, null=True, verbose_name='Nombre del Paciente'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='Sexo',
            field=models.CharField(max_length=100, null=True, verbose_name='Sexo'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='Telefono',
            field=models.CharField(max_length=100, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='archivos',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='archivos', verbose_name='Identificacion'),
        ),
    ]

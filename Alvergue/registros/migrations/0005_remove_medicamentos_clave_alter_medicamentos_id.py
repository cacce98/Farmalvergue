# Generated by Django 4.0.5 on 2022-07-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_alter_medicamentos_imagen_delete_salida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamentos',
            name='clave',
        ),
        migrations.AlterField(
            model_name='medicamentos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Clave'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0012_remove_archivos_titulo_archivos_nombremedic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivos',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='Precio'),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='sipnosis',
            field=models.TextField(max_length=300),
        ),
    ]
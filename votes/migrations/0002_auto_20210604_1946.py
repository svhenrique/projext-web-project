# Generated by Django 3.2.3 on 2021-06-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camaravoto',
            name='nome',
            field=models.CharField(max_length=30, unique=True, verbose_name='Nome da Camara de Votos'),
        ),
        migrations.AlterField(
            model_name='objeto',
            name='votos',
            field=models.IntegerField(default=0, verbose_name='Votos'),
        ),
    ]

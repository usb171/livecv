# Generated by Django 2.0.7 on 2018-08-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='tipo',
            field=models.CharField(max_length=10, null=True, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='sala',
            name='nome',
            field=models.CharField(max_length=10, null=True, verbose_name='Nome'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-08-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0006_auto_20180815_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='nome',
            field=models.CharField(max_length=20, null=True, verbose_name='Nome'),
        ),
    ]

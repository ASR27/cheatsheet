# Generated by Django 3.0.2 on 2020-04-13 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hojapersonaje', '0003_campaña_usucam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participa',
            name='dmPar',
        ),
    ]

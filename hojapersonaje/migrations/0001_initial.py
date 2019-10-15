# Generated by Django 2.2.6 on 2019-10-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaña',
            fields=[
                ('idCam', models.AutoField(primary_key=True, serialize=False)),
                ('nomCam', models.CharField(max_length=100)),
                ('desCam', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('idCar', models.AutoField(primary_key=True, serialize=False)),
                ('nomCar', models.CharField(max_length=20)),
                ('abCar', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Dote',
            fields=[
                ('idDot', models.AutoField(primary_key=True, serialize=False)),
                ('nomDot', models.CharField(max_length=100)),
                ('desDot', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('idHab', models.AutoField(primary_key=True, serialize=False)),
                ('nomHab', models.CharField(max_length=30)),
                ('modHab', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('idPer', models.AutoField(primary_key=True, serialize=False)),
                ('nomPer', models.CharField(max_length=40)),
                ('claPer', models.CharField(max_length=20)),
                ('nivPer', models.IntegerField(verbose_name=2)),
                ('razPer', models.CharField(max_length=20)),
                ('genPer', models.CharField(max_length=10)),
                ('aliPer', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsu', models.AutoField(primary_key=True, serialize=False)),
                ('nomUsu', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rasgo',
            fields=[
                ('idRas', models.AutoField(primary_key=True, serialize=False)),
                ('valRas', models.IntegerField(verbose_name=2)),
                ('carRas', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Caracteristica')),
                ('perRas', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Personaje')),
            ],
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('idRan', models.AutoField(primary_key=True, serialize=False)),
                ('valRan', models.IntegerField(verbose_name=2)),
                ('habRan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Habilidad')),
                ('perRan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Personaje')),
            ],
        ),
        migrations.CreateModel(
            name='Participa',
            fields=[
                ('idPar', models.AutoField(primary_key=True, serialize=False)),
                ('dmPar', models.BooleanField(default=False)),
                ('camPar', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Campaña')),
                ('usuPar', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cualidad',
            fields=[
                ('idCua', models.AutoField(primary_key=True, serialize=False)),
                ('dotCua', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Dote')),
                ('perCua', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Personaje')),
            ],
        ),
    ]

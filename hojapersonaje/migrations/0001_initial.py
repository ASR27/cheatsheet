# Generated by Django 3.0.2 on 2020-04-30 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaña',
            fields=[
                ('idCam', models.AutoField(primary_key=True, serialize=False)),
                ('nomCam', models.CharField(max_length=100)),
                ('desCam', models.CharField(max_length=5000)),
                ('finiCam', models.DateField(auto_now_add=True)),
                ('ffinCam', models.DateField(blank=True, null=True)),
                ('estCam', models.CharField(choices=[('Activo', 'Activo'), ('Sin comenzar', 'Sin comenzar'), ('En pausa', 'En pausa'), ('Finalizado', 'Finalizado')], default='Sin comenzar', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgPer', models.ImageField(blank=True, upload_to='avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('idPer', models.AutoField(primary_key=True, serialize=False)),
                ('nomPer', models.CharField(max_length=40)),
                ('claPer', models.CharField(max_length=20)),
                ('nivPer', models.IntegerField(blank=True, null=True)),
                ('razPer', models.CharField(max_length=20)),
                ('genPer', models.CharField(max_length=10)),
                ('aliPer', models.CharField(max_length=20)),
                ('ataPer', models.IntegerField(blank=True, null=True)),
                ('DGPer', models.IntegerField(blank=True, null=True)),
                ('MaxDGPer', models.IntegerField(blank=True, null=True)),
                ('FUE', models.IntegerField(blank=True, null=True)),
                ('DES', models.IntegerField(blank=True, null=True)),
                ('CON', models.IntegerField(blank=True, null=True)),
                ('INT', models.IntegerField(blank=True, null=True)),
                ('SAB', models.IntegerField(blank=True, null=True)),
                ('CAR', models.IntegerField(blank=True, null=True)),
                ('fortaleza', models.IntegerField(blank=True, null=True)),
                ('reflejos', models.IntegerField(blank=True, null=True)),
                ('voluntad', models.IntegerField(blank=True, null=True)),
                ('abrirCerraduras', models.IntegerField(blank=True, null=True)),
                ('artesania', models.IntegerField(blank=True, null=True)),
                ('averiguarIntenciones', models.IntegerField(blank=True, null=True)),
                ('avistar', models.IntegerField(blank=True, null=True)),
                ('buscar', models.IntegerField(blank=True, null=True)),
                ('concentracion', models.IntegerField(blank=True, null=True)),
                ('conocimientoConjuros', models.IntegerField(blank=True, null=True)),
                ('descifrarEscrituras', models.IntegerField(blank=True, null=True)),
                ('diplomacia', models.IntegerField(blank=True, null=True)),
                ('disfrazarse', models.IntegerField(blank=True, null=True)),
                ('engañar', models.IntegerField(blank=True, null=True)),
                ('equilibrio', models.IntegerField(blank=True, null=True)),
                ('esconderse', models.IntegerField(blank=True, null=True)),
                ('escuchar', models.IntegerField(blank=True, null=True)),
                ('falsificar', models.IntegerField(blank=True, null=True)),
                ('interpretar', models.IntegerField(blank=True, null=True)),
                ('intimidar', models.IntegerField(blank=True, null=True)),
                ('inutilizarMecanismo', models.IntegerField(blank=True, null=True)),
                ('juegoManos', models.IntegerField(blank=True, null=True)),
                ('montar', models.IntegerField(blank=True, null=True)),
                ('moverseSigilosamente', models.IntegerField(blank=True, null=True)),
                ('nadar', models.IntegerField(blank=True, null=True)),
                ('oficio', models.IntegerField(blank=True, null=True)),
                ('piruetas', models.IntegerField(blank=True, null=True)),
                ('reunirInformacion', models.IntegerField(blank=True, null=True)),
                ('saber', models.IntegerField(blank=True, null=True)),
                ('saltar', models.IntegerField(blank=True, null=True)),
                ('sanar', models.IntegerField(blank=True, null=True)),
                ('supervivencia', models.IntegerField(blank=True, null=True)),
                ('tasacion', models.IntegerField(blank=True, null=True)),
                ('tratoAnimales', models.IntegerField(blank=True, null=True)),
                ('trepar', models.IntegerField(blank=True, null=True)),
                ('usarObjetoMagico', models.IntegerField(blank=True, null=True)),
                ('usoCuerdas', models.IntegerField(blank=True, null=True)),
                ('ultimaTirada', models.IntegerField(blank=True, null=True)),
                ('ultimoCampo', models.CharField(blank=True, max_length=50, null=True)),
                ('camPer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Campaña')),
                ('usuPer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Participa',
            fields=[
                ('idPar', models.AutoField(primary_key=True, serialize=False)),
                ('camPar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Campaña')),
                ('usuPar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Perfil')),
            ],
        ),
        migrations.AddField(
            model_name='campaña',
            name='usuCam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hojapersonaje.Perfil'),
        ),
    ]

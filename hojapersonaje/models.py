from django.db import models

# Create your models here.

class Usuario(models.model):
	idUsu = models.AutoField(primary_key=True)
	nomUsu = models.CharField(max_length=40)
	email = models.EmailField(max_length=200)

class Campaña(models.model):
	idCam = models.AutoField(primary_key=True)
	nomCam = models.CharField(max_length=100)
	desCam = models.CharField(max_length=5000)

class Personaje(models.model):
	idPer  = models.AutoField(primary_key=True)
	nomPer = models.CharField(max_length=40)
	claPer = models.CharField(max_length=20)
	nivPer = models.IntegerField(2)
	razPer = models.CharField(max_length=20)
	genPer = models.
	aliPer = models.CharField(max_length=20)

class Caracteristica(models.model):
	idCar = models.AutoField(primary_key=True)
	nomCar = models.CharField(max_length=20)
	abCar = models.CharField(max_length=3)

class Habilidad(models.model):
	idHab = models.AutoField(primary_key=True)
	nomHab = models.CharField(max_length=30)
	modHab = models.CharField(max_length=3)

class Dote(models.model):
	idDot = models.AutoField(primary_key=True)
	nomDot = models.CharField(max_length=100)
	desDot = models.CharField(max_length=5000)

class Participa(models.model):
	usuPar = models.ManyToManyField(Usuario)
	camPar = models.ManyToManyField(Campaña)
	dmPar = models.BooleanField(default=False)

class Rasgo(models.model):
	perRas = models.ManyToManyField(Personaje)
	carRas = models.ManyToManyField(Caracteristica)
	valRas = models.IntegerField(2)

class Rango(models.model):
	perRan = models.ManyToManyField(Personaje)
	habRan = models.ManyToManyField(Habilidad)
	valRan = models.IntegerField(2)

class Cualidad(models.model):
	perCua = models.ManyToManyField(Personaje)
	dotCua = models.ManyToManyField(Dote)

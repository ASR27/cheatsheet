from django.db import models

# Create your models here.

class Usuario(models.Model):
	idUsu = models.AutoField(primary_key=True)
	nomUsu = models.CharField(max_length=40)
	email = models.EmailField(max_length=200)

	def __str__(self):
		return self.nomUsu

class Campaña(models.Model):
	idCam = models.AutoField(primary_key=True)
	nomCam = models.CharField(max_length=100)
	desCam = models.CharField(max_length=5000)

	def __str__(self):
		return self.nomCam

class Personaje(models.Model):
	idPer  = models.AutoField(primary_key=True)
	nomPer = models.CharField(max_length=40)
	claPer = models.CharField(max_length=20)
	nivPer = models.IntegerField(2)
	razPer = models.CharField(max_length=20)
	genPer = models.CharField(max_length=10)
	aliPer = models.CharField(max_length=20)

	def __str__(self):
		return self.nomPer

class Caracteristica(models.Model):
	idCar = models.AutoField(primary_key=True)
	nomCar = models.CharField(max_length=20)
	abCar = models.CharField(max_length=3)

	def __str__(self):
		return self.nomCar

class Habilidad(models.Model):
	idHab = models.AutoField(primary_key=True)
	nomHab = models.CharField(max_length=30)
	modHab = models.CharField(max_length=3)

	def __str__(self):
		return self.nomHab

class Dote(models.Model):
	idDot = models.AutoField(primary_key=True)
	nomDot = models.CharField(max_length=100)
	desDot = models.CharField(max_length=5000)

	def __str__(self):
		return self.nomDot

class Participa(models.Model):
	usuPar = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
	camPar = models.ForeignKey(Campaña, on_delete=models.CASCADE, default=1)
	dmPar = models.BooleanField(default=False)

	def __str__(self):
		return str(self.camPar)

class Rasgo(models.Model):
	perRas = models.ForeignKey(Personaje, on_delete=models.CASCADE, default=1)
	carRas = models.ForeignKey(Caracteristica, on_delete=models.CASCADE, default=1)
	valRas = models.IntegerField(2)

	def __str__(self):
		return self.perRas

class Rango(models.Model):
	perRan = models.ForeignKey(Personaje, on_delete=models.CASCADE, default=1)
	habRan = models.ForeignKey(Habilidad, on_delete=models.CASCADE, default=1)
	valRan = models.IntegerField(2)

	def __str__(self):
		return self.perRan

class Cualidad(models.Model):
	perCua = models.ForeignKey(Personaje, on_delete=models.CASCADE, default=1)
	dotCua = models.ForeignKey(Dote, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.perCua


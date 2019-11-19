from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Usuario de Django extendido

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	imgPer = models.ImageField(upload_to='avatar', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.create(user=instance)
	instance.perfil.save()


# Tablas creadas desde 0

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
	idPar = models.AutoField(primary_key=True)
	usuPar = models.OneToOneField(User, on_delete=models.CASCADE)
	camPar = models.ForeignKey(Campaña, on_delete=models.CASCADE)
	dmPar = models.BooleanField(default=False)

	def __str__(self):
		return str(self.camPar)

class Rasgo(models.Model):
	idRas = models.AutoField(primary_key=True)
	perRas = models.ForeignKey(Personaje, on_delete=models.CASCADE)
	carRas = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
	valRas = models.IntegerField(2)

	def __str__(self):
		return self.perRas

class Rango(models.Model):
	idRan = models.AutoField(primary_key=True)
	perRan = models.ForeignKey(Personaje, on_delete=models.CASCADE)
	habRan = models.ForeignKey(Habilidad, on_delete=models.CASCADE)
	valRan = models.IntegerField(2)

	def __str__(self):
		return self.perRan

class Cualidad(models.Model):
	idCua = models.AutoField(primary_key=True)
	perCua = models.ForeignKey(Personaje, on_delete=models.CASCADE)
	dotCua = models.ForeignKey(Dote, on_delete=models.CASCADE)

	def __str__(self):
		return self.perCua


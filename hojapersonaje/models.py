from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

# Usuario de Django extendido

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	imgPer = models.ImageField(upload_to='avatar', blank=True)

	def __str__(self):
		return str(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.create(user=instance)
	instance.perfil.save()


# Tablas creadas desde 0

ACT = "Activo"
SCO = "Sin comenzar"
PAU = "En pausa"
FIN = "Finalizado"

estado = (
	(ACT, "Activo"),
	(SCO, "Sin comenzar"),
	(PAU, "En pausa"),
	(FIN, "Finalizado"),
)


class Campaña(models.Model):
	

	idCam = models.AutoField(primary_key=True)
	nomCam = models.CharField(max_length=100)
	desCam = models.CharField(max_length=5000)
	usuCam = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	finiCam = models.DateField(auto_now_add=True)
	ffinCam = models.DateField(blank=True, null=True)
	estCam = models.CharField(max_length=20, choices=estado, default=SCO)

	def __str__(self):
		return str(self.nomCam)


class Personaje(models.Model):
	idPer  = models.AutoField(primary_key=True)
	nomPer = models.CharField(max_length=40)
	claPer = models.CharField(max_length=20)
	nivPer = models.IntegerField(blank=True, null=True)
	razPer = models.CharField(max_length=20)
	genPer = models.CharField(max_length=10)
	aliPer = models.CharField(max_length=20)
	ataPer = models.IntegerField(blank=True, null=True)
	DGPer = models.IntegerField(blank=True, null=True)
	MaxDGPer = models.IntegerField(blank=True, null=True)
	CAPer = models.IntegerField(blank=True, null=True)

	camPer = models.ForeignKey(Campaña, on_delete=models.CASCADE, blank=True, null=True)
	usuPer = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)

	FUE = models.IntegerField(blank=True, null=True)
	DES = models.IntegerField(blank=True, null=True)
	CON = models.IntegerField(blank=True, null=True)
	INT = models.IntegerField(blank=True, null=True)
	SAB = models.IntegerField(blank=True, null=True)
	CAR = models.IntegerField(blank=True, null=True)

	fortaleza = models.IntegerField(blank=True, null=True)
	reflejos = models.IntegerField(blank=True, null=True)
	voluntad = models.IntegerField(blank=True, null=True)
	abrirCerraduras = models.IntegerField(blank=True, null=True)
	artesania = models.IntegerField(blank=True, null=True)
	averiguarIntenciones = models.IntegerField(blank=True, null=True)
	avistar = models.IntegerField(blank=True, null=True)
	buscar = models.IntegerField(blank=True, null=True)
	concentracion = models.IntegerField(blank=True, null=True)
	conocimientoConjuros = models.IntegerField(blank=True, null=True)
	descifrarEscrituras = models.IntegerField(blank=True, null=True)
	diplomacia = models.IntegerField(blank=True, null=True)
	disfrazarse = models.IntegerField(blank=True, null=True)
	engañar = models.IntegerField(blank=True, null=True)
	equilibrio = models.IntegerField(blank=True, null=True)
	esconderse = models.IntegerField(blank=True, null=True)
	escuchar = models.IntegerField(blank=True, null=True)
	falsificar = models.IntegerField(blank=True, null=True)
	interpretar = models.IntegerField(blank=True, null=True)
	intimidar = models.IntegerField(blank=True, null=True)
	inutilizarMecanismo = models.IntegerField(blank=True, null=True)
	juegoManos = models.IntegerField(blank=True, null=True)
	montar = models.IntegerField(blank=True, null=True)
	moverseSigilosamente = models.IntegerField(blank=True, null=True)
	nadar = models.IntegerField(blank=True, null=True)
	oficio = models.IntegerField(blank=True, null=True)
	piruetas = models.IntegerField(blank=True, null=True)
	reunirInformacion = models.IntegerField(blank=True, null=True)
	saber = models.IntegerField(blank=True, null=True)
	saltar = models.IntegerField(blank=True, null=True)
	sanar = models.IntegerField(blank=True, null=True)
	supervivencia = models.IntegerField(blank=True, null=True)
	tasacion = models.IntegerField(blank=True, null=True)
	tratoAnimales = models.IntegerField(blank=True, null=True)
	trepar = models.IntegerField(blank=True, null=True)
	usarObjetoMagico = models.IntegerField(blank=True, null=True)
	usoCuerdas = models.IntegerField(blank=True, null=True)

	ultimaTirada = models.IntegerField(blank=True, null=True)
	ultimoCampo = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return str(self.nomPer)

class Participa(models.Model):
	idPar = models.AutoField(primary_key=True)
	usuPar = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	camPar = models.ForeignKey(Campaña, on_delete=models.CASCADE, blank=True, null=True)
	perPar = models.ForeignKey(Personaje, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return str(self.camPar)



#models.IntegerField(blank=True, null=True)
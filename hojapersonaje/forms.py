from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import formset_factory, PasswordInput, ModelChoiceField, Textarea, SelectDateWidget, ModelForm

from .models import *
from .models import estado

class Registro(UserCreationForm):
	imgPer = forms.ImageField(required=False)
	class Meta:
		model = User
		fields = (
			'username',
			'password1',
			'password2',
			'imgPer',
			)

class InicioSesion(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=PasswordInput())

class CampañasAddForm(forms.Form):
	nomCam = forms.CharField(max_length=100)
	desCam = forms.CharField(max_length=5000, widget=Textarea())
	ffinCam = forms.DateField(widget=SelectDateWidget())
	estCam = forms.ChoiceField(choices=estado)

class ParticipaCreateForm(forms.Form):
	usuPar = forms.ModelChoiceField(queryset=Perfil.objects.all())
	camPar = forms.ModelChoiceField(queryset=Campaña.objects.all())

class ParticipaUpdateForm(forms.ModelForm):
	class Meta:
		model = Participa
		fields = ['perPar']

	def __init__(self, *args, **kwargs):
		usuPer = kwargs.pop('usuPer')
		usuario = kwargs.pop('usuario')
		super(ParticipaUpdateForm, self).__init__(*args, **kwargs)
		self.fields['perPar'].queryset = Personaje.objects.all().filter(usuPer=usuario)


class EstadisticasAddForm(forms.Form):
	camPer = forms.ModelChoiceField(queryset=Campaña.objects.all(), required=False)
	nomPer = forms.CharField(max_length=40)
	claPer = forms.CharField(max_length=20)
	nivPer = forms.IntegerField()
	razPer = forms.CharField(max_length=20)
	genPer = forms.CharField(max_length=10)
	aliPer = forms.CharField(max_length=20)
	ataPer = forms.IntegerField()
	DGPer = forms.IntegerField()
	MaxDGPer = forms.IntegerField()
	CAPer = forms.IntegerField()
	FUE = forms.IntegerField()
	DES = forms.IntegerField()
	CON = forms.IntegerField()
	INT = forms.IntegerField()
	SAB = forms.IntegerField()
	CAR = forms.IntegerField()
	fortaleza = forms.IntegerField()
	reflejos = forms.IntegerField()
	voluntad = forms.IntegerField()
	abrirCerraduras = forms.IntegerField()
	artesania = forms.IntegerField()
	averiguarIntenciones = forms.IntegerField()
	avistar = forms.IntegerField()
	buscar = forms.IntegerField()
	concentracion = forms.IntegerField()
	conocimientoConjuros = forms.IntegerField()
	descifrarEscrituras = forms.IntegerField()
	diplomacia = forms.IntegerField()
	disfrazarse = forms.IntegerField()
	engañar = forms.IntegerField()
	equilibrio = forms.IntegerField()
	esconderse = forms.IntegerField()
	escuchar = forms.IntegerField()
	falsificar = forms.IntegerField()
	interpretar = forms.IntegerField()
	intimidar = forms.IntegerField()
	inutilizarMecanismo = forms.IntegerField()
	juegoManos = forms.IntegerField()
	montar = forms.IntegerField()
	moverseSigilosamente = forms.IntegerField()
	nadar = forms.IntegerField()
	oficio = forms.IntegerField()
	piruetas = forms.IntegerField()
	reunirInformacion = forms.IntegerField()
	saber = forms.IntegerField()
	saltar = forms.IntegerField()
	sanar = forms.IntegerField()
	supervivencia = forms.IntegerField()
	tasacion = forms.IntegerField()
	tratoAnimales = forms.IntegerField()
	trepar = forms.IntegerField()
	usarObjetoMagico = forms.IntegerField()
	usoCuerdas = forms.IntegerField()
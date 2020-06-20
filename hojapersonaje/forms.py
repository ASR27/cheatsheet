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
	FUE = forms.IntegerField(initial=0)
	DES = forms.IntegerField(initial=0)
	CON = forms.IntegerField(initial=0)
	INT = forms.IntegerField(initial=0)
	SAB = forms.IntegerField(initial=0)
	CAR = forms.IntegerField(initial=0)
	fortaleza = forms.IntegerField(initial=0)
	reflejos = forms.IntegerField(initial=0)
	voluntad = forms.IntegerField(initial=0)
	abrirCerraduras = forms.IntegerField(initial=0)
	artesania = forms.IntegerField(initial=0)
	averiguarIntenciones = forms.IntegerField(initial=0)
	avistar = forms.IntegerField(initial=0)
	buscar = forms.IntegerField(initial=0)
	concentracion = forms.IntegerField(initial=0)
	conocimientoConjuros = forms.IntegerField(initial=0)
	descifrarEscrituras = forms.IntegerField(initial=0)
	diplomacia = forms.IntegerField(initial=0)
	disfrazarse = forms.IntegerField(initial=0)
	engañar = forms.IntegerField(initial=0)
	equilibrio = forms.IntegerField(initial=0)
	esconderse = forms.IntegerField(initial=0)
	escuchar = forms.IntegerField(initial=0)
	falsificar = forms.IntegerField(initial=0)
	interpretar = forms.IntegerField(initial=0)
	intimidar = forms.IntegerField(initial=0)
	inutilizarMecanismo = forms.IntegerField(initial=0)
	juegoManos = forms.IntegerField(initial=0)
	montar = forms.IntegerField(initial=0)
	moverseSigilosamente = forms.IntegerField(initial=0)
	nadar = forms.IntegerField(initial=0)
	oficio = forms.IntegerField(initial=0)
	piruetas = forms.IntegerField(initial=0)
	reunirInformacion = forms.IntegerField(initial=0)
	saber = forms.IntegerField(initial=0)
	saltar = forms.IntegerField(initial=0)
	sanar = forms.IntegerField(initial=0)
	supervivencia = forms.IntegerField(initial=0)
	tasacion = forms.IntegerField(initial=0)
	tratoAnimales = forms.IntegerField(initial=0)
	trepar = forms.IntegerField(initial=0)
	usarObjetoMagico = forms.IntegerField(initial=0)
	usoCuerdas = forms.IntegerField(initial=0)

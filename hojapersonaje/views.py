from django.shortcuts import HttpResponse, render, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hojapersonaje.models import Participa
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from hojapersonaje.forms import Registro
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAdminUser
from hojapersonaje.serializers import *

from .models import *
from .forms import *

import random

# Create your views here.


###########################################
# Participa
###########################################


class ParticipaList(ListView):
	model = Participa
	template_name="hojapersonaje/participa_list.html"

class ParticipaDetail(DetailView):
	model = Participa
	template_name="hojapersonaje/participa_detail.html"
	fields = '__all__'

	def get_content_data(self, **kwargs):
		context = super().get_content_data(**kwargs)
		context['camPar']=self.camPar
		return 

@login_required(login_url='/accounts/login/')
def ParticipaCreate(request):
	if request.method == 'POST':
		form1 = ParticipaCreateForm(request.POST)
		if form1.is_valid():
			participa = Participa()
			participa.usuPar = form1.cleaned_data.get('usuPar')
			participa.camPar = form1.cleaned_data.get('camPar')
			if request.user.id == participa.camPar.usuCam.user.id:
				participa.save()
				return HttpResponseRedirect('/hojapersonaje/participalist')
			else:
				return HttpResponseRedirect('/hojapersonaje/errorparticipa')
	else:
		form1 = ParticipaCreateForm()
	return render(request, 'hojapersonaje/participa_form.html', {'participa': form1})


class ParticipaDelete(DeleteView):
	model = Participa
	fields = '__all__'
	success_url = reverse_lazy('participantes')
	template_name="hojapersonaje/participa_delete.html"

class ParticipaUpdate(UpdateView):
	model = Participa
	form_class = ParticipaUpdateForm
	#fields = ['perPar']
	success_url = reverse_lazy('participantes')
	template_name="hojapersonaje/participa_update.html"

	def get_form_kwargs(self):
		kwargs = super(ParticipaUpdate, self).get_form_kwargs()
		kwargs.update({'usuPer': self.kwargs.get('usuPer')})
		return kwargs



def ErrorParticipa(request):
	return HttpResponseRedirect('/hojapersonaje/errorparticipa')


###########################################
# Usuarios
###########################################



class UsuarioList(ListView):
	model = User
	template_name="hojapersonaje/usuario_list.html"

class UsuarioDetail(DetailView):
	model = User
	template_name="hojapersonaje/usuario_detail.html"
	fields = '__all__'

	def get_content_data(self, **kwargs):
		context = super().get_content_data(**kwargs)
		return

class UsuarioUpdate(UpdateView):
	model = Perfil
	fields = ['imgPer']
	template_name="hojapersonaje/usuarioupdate.html"
	success_url = reverse_lazy('usuarios')


###########################################
# Sign Up
###########################################


def signup(request):
	if request.method == 'POST':
		form = Registro(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user.perfil.imgPer = form.cleaned_data.get('imgPer')
			user.save()
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = Registro()
	return render(request, 'signup.html', {'form': form})



###########################################
# Hoja de personaje
###########################################



class Estadisticas(ListView):
	model = Personaje
	template_name="hojapersonaje/estadisticas.html"

class EstadisticasDetail(DetailView):
	model = Personaje
	template_name = "hojapersonaje/estadisticasdetail.html"
	fields = '__all__'

	def get_content_data(self, **kwargs):
		context = super().get_content_data(**kwargs)
		return

class EstadisticasUpdate(UpdateView):
	model = Personaje
	fields = ['nomPer',
	'claPer',
	'nivPer',
	'razPer',
	'genPer',
	'aliPer',
	'camPer',
	'FUE',
	'DES',
	'CON',
	'INT',
	'SAB',
	'CAR',
	'DGPer',
	'MaxDGPer',
	'fortaleza',
	'reflejos',
	'voluntad',
	'abrirCerraduras',
	'artesania',
	'averiguarIntenciones',
	'avistar',
	'buscar',
	'concentracion',
	'conocimientoConjuros',
	'descifrarEscrituras',
	'diplomacia',
	'disfrazarse',
	'engañar',
	'equilibrio',
	'esconderse',
	'escuchar',
	'falsificar',
	'interpretar',
	'intimidar',
	'inutilizarMecanismo',
	'juegoManos',
	'montar',
	'moverseSigilosamente',
	'nadar',
	'oficio',
	'piruetas',
	'reunirInformacion',
	'saber',
	'saltar',
	'sanar',
	'supervivencia',
	'tasacion',
	'tratoAnimales',
	'trepar',
	'usarObjetoMagico',
	'usoCuerdas']
	template_name="hojapersonaje/estadisticasupdate.html"
	success_url = reverse_lazy('estadisticas')


class EstadisticasDelete(DeleteView):
	model = Personaje
	fields = '__all__'
	success_url = reverse_lazy('estadisticas')
	template_name="hojapersonaje/estadisticasdelete.html"

@login_required(login_url='/accounts/login/')
def EstadisticasAdd(request):
	if request.method == 'POST':
		form1 = EstadisticasAddForm(request.POST)
		if form1.is_valid():
			personaje = Personaje()
			usuario = Perfil.objects.get(user=request.user)
			personaje.usuPer = usuario
			personaje.nomPer = form1.cleaned_data.get('nomPer')
			personaje.claPer = form1.cleaned_data.get('claPer')
			personaje.nivPer = form1.cleaned_data.get('nivPer')
			personaje.ataPer = form1.cleaned_data.get('ataPer')
			personaje.razPer = form1.cleaned_data.get('razPer')
			personaje.genPer = form1.cleaned_data.get('genPer')
			personaje.aliPer = form1.cleaned_data.get('aliPer')
			personaje.DGPer = form1.cleaned_data.get('DGPer')
			personaje.MaxDGPer = form1.cleaned_data.get('MaxDGPer')
			personaje.CAPer = form1.cleaned_data.get('CAPer')

			personaje.FUE = form1.cleaned_data.get('FUE')
			personaje.DES = form1.cleaned_data.get('DES')
			personaje.CON = form1.cleaned_data.get('CON')
			personaje.INT = form1.cleaned_data.get('INT')
			personaje.SAB = form1.cleaned_data.get('SAB')
			personaje.CAR = form1.cleaned_data.get('CAR')
			
			personaje.fortaleza = form1.cleaned_data.get('fortaleza')
			personaje.reflejos = form1.cleaned_data.get('reflejos')
			personaje.voluntad = form1.cleaned_data.get('voluntad')

			personaje.abrirCerraduras = form1.cleaned_data.get('abrirCerraduras')
			personaje.artesania = form1.cleaned_data.get('artesania')
			personaje.averiguarIntenciones = form1.cleaned_data.get('averiguarIntenciones')
			personaje.avistar = form1.cleaned_data.get('avistar')
			personaje.buscar = form1.cleaned_data.get('buscar')
			personaje.concentracion = form1.cleaned_data.get('concentracion')
			personaje.conocimientoConjuros = form1.cleaned_data.get('conocimientoConjuros')
			personaje.descifrarEscrituras = form1.cleaned_data.get('descifrarEscrituras')
			personaje.diplomacia = form1.cleaned_data.get('diplomacia')
			personaje.disfrazarse = form1.cleaned_data.get('disfrazarse')
			personaje.engañar = form1.cleaned_data.get('engañar')
			personaje.equilibrio = form1.cleaned_data.get('equilibrio')
			personaje.esconderse = form1.cleaned_data.get('esconderse')
			personaje.escuchar = form1.cleaned_data.get('escuchar')
			personaje.falsificar = form1.cleaned_data.get('falsificar')
			personaje.interpretar = form1.cleaned_data.get('interpretar')
			personaje.intimidar = form1.cleaned_data.get('intimidar')
			personaje.inutilizarMecanismo = form1.cleaned_data.get('inutilizarMecanismo')
			personaje.juegoManos = form1.cleaned_data.get('juegoManos')
			personaje.montar = form1.cleaned_data.get('montar')
			personaje.moverseSigilosamente = form1.cleaned_data.get('moverseSigilosamente')
			personaje.nadar = form1.cleaned_data.get('nadar')
			personaje.oficio = form1.cleaned_data.get('oficio')
			personaje.piruetas = form1.cleaned_data.get('piruetas')
			personaje.reunirInformacion = form1.cleaned_data.get('reunirInformacion')
			personaje.saber = form1.cleaned_data.get('saber')
			personaje.saltar = form1.cleaned_data.get('saltar')
			personaje.sanar = form1.cleaned_data.get('sanar')
			personaje.supervivencia = form1.cleaned_data.get('supervivencia')
			personaje.tasacion = form1.cleaned_data.get('tasacion')
			personaje.tratoAnimales = form1.cleaned_data.get('tratoAnimales')
			personaje.trepar = form1.cleaned_data.get('trepar')
			personaje.usarObjetoMagico = form1.cleaned_data.get('usarObjetoMagico')
			personaje.usoCuerdas = form1.cleaned_data.get('usoCuerdas')

			personaje.save()
			return HttpResponseRedirect('/hojapersonaje/estadisticas')
	else:
		form1 = EstadisticasAddForm()
	return render(request, 'hojapersonaje/estadisticasadd.html', {'personaje': form1})



###########################################
# Campañas
###########################################



class Campañas(ListView):
	model = Campaña
	template_name="hojapersonaje/campañas.html"

class CampañasDetail(DetailView):
	model = Campaña
	template_name = "hojapersonaje/campañasdetail.html"
	fields = '__all__'

class CampañasUpdate(UpdateView):
	model = Campaña
	fields = ['nomCam','desCam', 'ffinCam', 'estCam']
	template_name="hojapersonaje/campañasupdate.html"
	success_url = reverse_lazy('campañas')

class CampañasDelete(DeleteView):
	model = Campaña
	fields = '__all__'
	success_url = reverse_lazy('campañas')
	template_name="hojapersonaje/campañasdelete.html"

@login_required(login_url='/accounts/login/')
def CampañasAdd(request):
	if request.method == 'POST':
		form1 = CampañasAddForm(request.POST)
		if form1.is_valid():
			campaña = Campaña()
			usuario = Perfil.objects.get(user=request.user)
			campaña.usuCam = usuario
			campaña.nomCam = form1.cleaned_data.get('nomCam')
			campaña.desCam = form1.cleaned_data.get('desCam')
			campaña.ffinCam = form1.cleaned_data.get('ffinCam')
			campaña.estCam = form1.cleaned_data.get('estCam')
						
			campaña.save()
			return HttpResponseRedirect('/hojapersonaje/campanas')
	else:
		form1 = CampañasAddForm()
	return render(request, 'hojapersonaje/campañasadd.html', {'campaña': form1})


###########################################
# Funcion para tirar dado
###########################################


def PersonajeBoton(request):
	col = request.GET.get('columna')
	dado = random.randint(1,20)
	id = request.GET.get('id')
	queryset = Personaje.objects.get(idPer=id)
	queryset.ultimaTirada = dado
	queryset.ultimoCampo = col
	queryset.save()
	return HttpResponseRedirect('/hojapersonaje/estadisticasdetail/' + id)


###########################################
# API
###########################################



class UserAPI(viewsets.ModelViewSet):
	"""
	API
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAdminUser]

class CampañaAPI(viewsets.ModelViewSet):
	"""
	API
	"""
	queryset = Campaña.objects.all()
	serializer_class = CampañaSerializer
	permission_classes = [IsAdminUser]

class PersonajeAPI(viewsets.ModelViewSet):
	"""
	API
	"""
	queryset = Personaje.objects.all()
	serializer_class = PersonajeSerializer
	permission_classes = [IsAdminUser]

class ParticipaAPI(viewsets.ModelViewSet):
	"""
	API
	"""
	queryset = Participa.objects.all()
	serializer_class = ParticipaSerializer
	permission_classes = [IsAdminUser]

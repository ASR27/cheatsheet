from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hojapersonaje.models import Participa
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from hojapersonaje.forms import Registro

from .models import *
from .forms import *

# Create your views here.

def index(request):
	return HttpResponse("Hello, world")

# Participa listas y detalles

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

# Pruebas crear, actualizar y borrar

class ParticipaCreate(CreateView):
	model = Participa
	fields = '__all__'
	template_name="hojapersonaje/participa_form.html"
	success_url = reverse_lazy('participantes')

class ParticipaUpdate(UpdateView):
	model = Participa
	fields = '__all__'
	template_name="hojapersonaje/participa_update.html"
	success_url = reverse_lazy('participantes')

class ParticipaDelete(DeleteView):
	model = Participa
	fields = '__all__'
	success_url = reverse_lazy('participantes')
	template_name="hojapersonaje/participa_delete.html"

# Usuarios lista y detalles

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

# Sign Up, temporalmente redirige a la lista de usuarios

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
			return redirect('usuarios')
	else:
		form = Registro()
	return render(request, 'signup.html', {'form': form})


# def InicioSesion(request):
# 	if request.method == 'POST':
# 		form = InicioSesion(request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(request, username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				return redirect('usuarios')
# 			else:
# 				return HttpResponse("Error de Login")
# 	else:
# 		form = InicioSesion()
# 	return render(request, 'login.html', {'form': form})
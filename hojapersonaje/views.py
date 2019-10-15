from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from hojapersonaje.models import Participa, Usuario

# Create your views here.

def index(request):
	return HttpResponse("Hello, world")

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


class UsuarioList(ListView):
	model = Usuario
	template_name="hojapersonaje/usuario_list.html"

class UsuarioDetail(DetailView):
	model = Usuario
	template_name="hojapersonaje/usuario_detail.html"
	fields = '__all__'

	def get_content_data(self, **kwargs):
		context = super().get_content_data(**kwargs)
		return
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hojapersonaje.models import Participa
from django.contrib.auth.models import User

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
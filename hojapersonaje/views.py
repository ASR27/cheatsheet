from django.shortcuts import HttpResponse
from django.views.generic import ListView
from hojapersonaje.models import Participa

# Create your views here.

def index(request):
	return HttpResponse("Hello, world")

class ParticipaList(ListView):
	model = Participa
	template_name="/hojapersonaje/participa_list.html"
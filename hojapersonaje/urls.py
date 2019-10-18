from django.urls import path

from . import views
from hojapersonaje.views import *

urlpatterns = [
	path('', views.index, name="index"),
	path('participalist/', ParticipaList.as_view(), name="participantes"),
	path('participadetail/<int:pk>', ParticipaDetail.as_view(), name="participante"),
	path('usuariolist/', UsuarioList.as_view(), name="usuarios"),
	path('usuariodetail/<int:pk>', UsuarioDetail.as_view(), name="usuario_detail"),
]
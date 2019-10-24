from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views
from hojapersonaje.views import *

urlpatterns = [
	path('', views.index, name="index"),
	path('participalist/', ParticipaList.as_view(), name="participantes"),
	path('participadetail/<int:pk>', ParticipaDetail.as_view(), name="participante"),
	path('usuariolist/', UsuarioList.as_view(), name="usuarios"),
	path('usuariodetail/<int:pk>', UsuarioDetail.as_view(), name="usuario_detail"),
	path('participa_add/', ParticipaCreate.as_view(), name='participa-add'),
	path(r'participa_update/(?P<pk>[0-9]+)/$', ParticipaUpdate.as_view(), name='participa-update'),
	path(r'participa_delete/(?P<pk>[0-9]+)/delete/$', ParticipaDelete.as_view(), name='participa-delete'),
]
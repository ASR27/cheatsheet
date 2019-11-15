from django.urls import path, re_path, include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views
from hojapersonaje.views import *

urlpatterns = [
	path('', views.index, name="index"),
	path('participalist/', ParticipaList.as_view(), name="participantes"),
	path('participadetail/<int:pk>', ParticipaDetail.as_view(), name="participante"),
	path('usuariolist/', UsuarioList.as_view(), name="usuarios"),
	path('usuariodetail/<int:pk>', UsuarioDetail.as_view(), name="usuario_detail"),
	path('participa_add/', ParticipaCreate.as_view(), name='participa-add'),
	path('participa_update/<int:pk>/', ParticipaUpdate.as_view(), name='participa-update'),
	path('participa_delete/<int:pk>/delete/', ParticipaDelete.as_view(), name='participa-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
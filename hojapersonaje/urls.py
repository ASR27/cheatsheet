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
	path('accounts/', include('django.contrib.auth.urls')),
	path('participalist/', ParticipaList.as_view(), name="participantes"),
	path('participadetail/<int:pk>', ParticipaDetail.as_view(), name="participante"),
	path('usuariolist/', UsuarioList.as_view(), name="usuarios"),
	path('usuariodetail/<int:pk>', UsuarioDetail.as_view(), name="usuario_detail"),
	path('usuarioupdate/<int:pk>', UsuarioUpdate.as_view(), name="usuarioupdate"),
	path('participa_add/', ParticipaCreate, name='participa-add'),
	path('participa_delete/<int:pk>/delete/', ParticipaDelete.as_view(), name='participa-delete'),
	path('participa_update/<int:pk>', ParticipaUpdate.as_view(), name='participaupdate'),
	path('estadisticas/', Estadisticas.as_view(), name='estadisticas'),
	path('estadisticasadd/', EstadisticasAdd, name='estadisticasadd'),
	path('estadisticasdetail/<int:pk>', EstadisticasDetail.as_view(), name='estadisticasdetail'),
	re_path('estadisticasupdate/(?P<pk>\d+)', EstadisticasUpdate.as_view(), name='estadisticasupdate'),
	path('estadisticasdelete/<int:pk>/delete', EstadisticasDelete.as_view(), name='estadisticasdelete'),
	path('campanas/', Campañas.as_view(), name='campañas'),
	path('campanasdetail/<int:pk>', CampañasDetail.as_view(), name='campanasdetail'),
	path('campanasadd/', CampañasAdd, name='campanasadd'),
	re_path('campanasupdate/(?P<pk>\d+)', CampañasUpdate.as_view(), name='campanasupdate'),
	path('campanasdelete/<int:pk>/delete', CampañasDelete.as_view(), name='campanasdelete'),
	path('errorparticipa/', TemplateView.as_view(template_name='hojapersonaje/errorparticipa.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
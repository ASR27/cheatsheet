from django.urls import path

from . import views
from hojapersonaje.views import *

urlpatterns = [
	path('', views.index, name="index"),
	path('participalist/', ParticipaList.as_view(), name="participantes"),
]
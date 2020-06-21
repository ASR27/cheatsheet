"""cheatsheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from hojapersonaje.views import *
from hojapersonaje import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'userapi', views.UserAPI)
router.register(r'campañaapi', views.CampañaAPI)
router.register(r'personajeapi', views.PersonajeAPI)
router.register(r'participaapi', views.ParticipaAPI)


urlpatterns = [
	url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('hojapersonaje/', include('hojapersonaje.urls')),
    url('signup/', signup, name='signup'),
    url('personajeboton/', PersonajeBoton, name='personajeboton'),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    path('', include('hojapersonaje.urls')),
    path('', include(router.urls)),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import formset_factory, PasswordInput

from .models import *

class Registro(UserCreationForm):
	imgPer = forms.ImageField(required=False)
	class Meta:
		model = User
		fields = (
			'username',
			'password1',
			'password2',
			'imgPer',
			)

class InicioSesion(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=PasswordInput())
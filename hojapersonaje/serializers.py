from django.contrib.auth.models import User, Group
from rest_framework import serializers
from hojapersonaje.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username']

class CampañaSerializer(serializers.HyperlinkedModelSerializer):
	usuCam = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Campaña
		fields = '__all__'

class PersonajeSerializer(serializers.HyperlinkedModelSerializer):
	usuPer = serializers.PrimaryKeyRelatedField(read_only=True)
	camPer = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Personaje
		fields = '__all__'

class ParticipaSerializer(serializers.HyperlinkedModelSerializer):
	usuPar = serializers.PrimaryKeyRelatedField(read_only=True)
	camPar = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Participa
		fields = '__all__'
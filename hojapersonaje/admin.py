from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Caracteristica
from .models import Campaña
from .models import Participa

admin.site.register(Caracteristica)
admin.site.register(Campaña)
admin.site.register(Participa)

# Register your models here.

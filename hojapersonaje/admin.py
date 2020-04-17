from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *


admin.site.register(Campaña)
admin.site.register(Participa)
admin.site.register(Personaje)


class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)    	

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.

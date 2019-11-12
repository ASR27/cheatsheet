from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Caracteristica
from .models import Campaña
from .models import Participa
from .models import Perfil

admin.site.register(Caracteristica)
admin.site.register(Campaña)
admin.site.register(Participa)

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)    	

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.

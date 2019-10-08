from django.contrib import admin

from .models import Caracteristica
from .models import Usuario
from .models import Campaña
from .models import Participa

admin.site.register(Caracteristica)
admin.site.register(Usuario)
admin.site.register(Campaña)
admin.site.register(Participa)

# Register your models here.

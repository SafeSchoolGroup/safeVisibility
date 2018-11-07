from django.contrib import admin

# Register your models here.

from .models import Classe
from .models import Etablissement

admin.site.register(Classe)

admin.site.register(Etablissement)

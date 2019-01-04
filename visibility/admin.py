from django.contrib import admin

# Register your models here.

from .models import Classe, Etablissement, Serie, Specialite, Niveau

admin.site.register(Classe)

admin.site.register(Etablissement)

admin.site.register(Serie)

admin.site.register(Specialite)

admin.site.register(Niveau)
from django.contrib import admin

from .models import Persona, Coeval, Curso

admin.site.register(Persona)
admin.site.register(Coeval)
admin.site.register(Curso)
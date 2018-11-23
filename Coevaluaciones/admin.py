from django.contrib import admin

from .models import Persona, Coeval, Curso, Rol, Integrante, Pregunta_Coeval, Pregunta, Respuesta, Estado

admin.site.register(Persona)
admin.site.register(Curso)
admin.site.register(Integrante)
admin.site.register(Rol)
admin.site.register(Pregunta)
admin.site.register(Coeval)
admin.site.register(Pregunta_Coeval)
admin.site.register(Respuesta)
admin.site.register(Estado)
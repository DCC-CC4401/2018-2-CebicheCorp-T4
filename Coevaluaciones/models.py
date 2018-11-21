from django.db import models
from django.conf import settings
from django.utils import timezone

class Persona(models.Model):
    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10)
    seccion = models.IntegerField()
    anno = models.IntegerField()
    semestre = models.IntegerField()
    estudiantes = models.ManyToManyField(Persona, related_name='persona_estudiantes')
    profesores = models.ManyToManyField(Persona, related_name='persona_profesores')
    cuerpo_docente = models.ManyToManyField(Persona, related_name='persona_cuerpo_docente', blank=True)

class Coeval(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField('fecha de inicio')
    fecha_termino = models.DateTimeField('fecha de término')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
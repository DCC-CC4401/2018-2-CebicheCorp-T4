from django.db import models


class Persona(models.Model):
    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10)
    seccion = models.IntegerField()
    anno = models.IntegerField()
    semestre = models.IntegerField()
    integrantes = models.ManyToManyField(Persona, through='Integrante')


class Rol(models.Model):
    rol = models.CharField(max_length=50)
    icono_archivo = models.CharField(max_length=50)


class Integrante(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)


class Pregunta(models.Model):
    texto = models.CharField(max_length=500)


class Coeval(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    preguntas = models.ManyToManyField(Pregunta, through='Pregunta_Coeval')


class Pregunta_Coeval(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    coeval = models.ForeignKey(Coeval, on_delete=models.CASCADE)
    orden = models.IntegerField()
    ponderacion = models.FloatField()

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta_Coeval, on_delete=models.CASCADE)
    nota = models.IntegerField()
    autor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='autor')
    evaluado = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='evaluado')

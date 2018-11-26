from django.db import models
from django.contrib.auth import get_user_model


class Persona(models.Model):
    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='persona')

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10)
    seccion = models.IntegerField()
    anno = models.IntegerField()
    semestre = models.IntegerField()
    integrantes = models.ManyToManyField(Persona, through='Integrante')

    def __str__(self):
        ret = self.codigo + "-" + str(self.seccion) + \
              " " + self.nombre + " " + str(self.anno) + "-" + str(self.semestre)
        return ret

    class Meta:
        ordering = ['-anno', '-semestre']
        unique_together = ['codigo', 'seccion', 'anno', 'semestre']


class Rol(models.Model):
    rol = models.CharField(max_length=50)
    css_class = models.CharField(max_length=50)

    def __str__(self):
        return self.rol


class Integrante(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        ret = str(self.persona) + " / " + str(self.curso)
        return ret


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    integrantes = models.ManyToManyField(Persona)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


class Pregunta(models.Model):
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto


class Estado(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.estado


class Coeval(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    preguntas = models.ManyToManyField(Pregunta, through='Pregunta_Coeval')

    def __str__(self):
        return self.titulo

class Pregunta_Coeval(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    coeval = models.ForeignKey(Coeval, on_delete=models.CASCADE)
    orden = models.IntegerField()
    ponderacion = models.FloatField()

    def __str__(self):
        ret = str(self.coeval) + " / " + str(self.pregunta)
        return ret

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta_Coeval, on_delete=models.CASCADE)
    nota = models.IntegerField()
    autor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='autor')
    evaluado = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='evaluado')
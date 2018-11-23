from django.shortcuts import render
from .models import Coeval, Curso, Integrante, Persona
from django.utils import timezone

def login(request):
    return render(request, 'login.html', {})

def index(request):
    integrante_de = Integrante.objects.filter(persona__rut='12345678-9').order_by('-curso__anno', '-curso__semestre')
#    mis_cursos = []
#    for integrante in integrante_de:
#        mis_cursos.append(integrante.curso)

    mis_cursos = Curso.objects.filter(integrantes__rut='12345678-9')

    ultimas_coeval = Coeval.objects.filter(curso__in=mis_cursos).order_by('-fecha_inicio')[:10]

    context = {'integrante_de': integrante_de, 'ultimas_coeval': ultimas_coeval}
    return render(request, 'index.html', context)

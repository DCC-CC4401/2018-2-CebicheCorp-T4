from django.shortcuts import render
from .models import Coeval, Curso, Integrante, Persona
from django.utils import timezone

def index(request):
    #Todas las relaciones Integrante de una persona
    integrante_de = Integrante.objects.filter(persona__rut='12345678-9').order_by('-curso__anno', '-curso__semestre')

    #Todos los cursos de una persona
    mis_cursos = Curso.objects.filter(integrantes__rut='12345678-9')

    #Crear lista de coevaluaciones de todos los cursos obtenidos, con su respectiva relación de Integrante
    ultimas_coeval = Coeval.objects.filter(curso__in=mis_cursos).order_by('-fecha_inicio')[:10]
    ultimas_coeval_integrante = []
    for coeval in ultimas_coeval:
        for integrante in integrante_de:
            if coeval.curso == integrante.curso:
                coeval_integrante = {'coeval': coeval, 'integrante': integrante}
                ultimas_coeval_integrante.append(coeval_integrante)

    context = {'integrante_de': integrante_de, 'ultimas_coeval_integrante': ultimas_coeval_integrante}
    return render(request, 'index.html', context)

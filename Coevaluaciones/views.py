from django.shortcuts import render, redirect
from .models import Coeval, Curso, Integrante, Persona
from django.utils import timezone


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user

    # Todas las relaciones Integrante de una persona
    integrante_de = Integrante.objects.filter(persona=user.persona).order_by('-curso__anno',
                                                                             '-curso__semestre')

    # Todos los cursos de una persona
    mis_cursos = Curso.objects.filter(integrantes=user.persona)

    # Crear lista de coevaluaciones de todos los cursos obtenidos, con su respectiva relación de Integrante
    ultimas_coeval = Coeval.objects.filter(curso__in=mis_cursos).order_by('-fecha_termino')[:10]
    ultimas_coeval_integrante = []
    for coeval in ultimas_coeval:
        for integrante in integrante_de:
            if coeval.curso == integrante.curso:
                docente = 1 if (integrante.rol_id in [2, 3, 4]) else 0
                coeval_integrante = {'coeval': coeval, 'integrante': integrante, 'docente': docente}
                ultimas_coeval_integrante.append(coeval_integrante)

    context = {'integrante_de': integrante_de, 'ultimas_coeval_integrante': ultimas_coeval_integrante}
    return render(request, 'index.html', context)


def ficha_curso(request, anno, semestre, codigo, seccion):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user

    curso = Curso.objects.get(anno=anno, semestre=semestre, codigo=codigo, seccion=seccion)
    integrante = Integrante.objects.get(persona=user.persona, curso=curso)
    coevals = Coeval.objects.filter(curso=curso).order_by('-fecha_termino')
    if semestre == 1:
        semestre_str = 'Otoño'
    elif semestre == 2:
        semestre_str = 'Primavera'
    elif semestre == 3:
        semestre_str = 'Verano'

    docente = 1 if (integrante.rol_id in [2, 3, 4]) else 0

    context = {'curso': curso, 'coevals': coevals, 'integrante': integrante, 'semestre_str': semestre_str, 'docente': docente}

    return render(request, 'ficha_curso.html', context)

def ficha_usuario(request, rut):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user

    mis_cursos = Curso.objects.filter(integrantes=user.persona)
    integrante_de = Integrante.objects.filter(persona=user.persona).order_by('-curso__anno',
                                                                             '-curso__semestre')
    context = {'usuario': user, 'mis_cursos': mis_cursos, 'integrante_de': integrante_de}
    return render(request, 'ficha_usuario.html', context)
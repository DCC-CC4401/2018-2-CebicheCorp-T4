from django.shortcuts import render
from .models import Coeval, Curso
from django.utils import timezone

def login(request):
    return render(request, 'login.html', {})

def index(request):
    ultimas_coeval = Coeval.objects.order_by('-fecha_inicio')[:5]
    context = {'ultimas_coeval': ultimas_coeval}
    return render(request, 'home.html', context)

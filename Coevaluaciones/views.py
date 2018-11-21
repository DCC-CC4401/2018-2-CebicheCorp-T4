from django.shortcuts import render
from .models import Post
from django.utils import timezone

def login(request):
    return render(request, 'Coevaluaciones/login.html', {})

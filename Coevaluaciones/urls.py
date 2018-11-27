from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('curso/<int:anno>/<int:semestre>/<slug:codigo>/<int:seccion>', views.ficha_curso, name='ficha_curso')
]
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'aluno'
urlpatterns = [
    path('perfil', views.editar_perfil, name='perfil'),
    path('todos', views.listar_alunos, name='listar_alunos'),
]

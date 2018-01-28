from django.urls import path
from . import views


app_name = 'professor'
urlpatterns = [
    path('perfil', views.editar_perfil, name='perfil'),
    path('todos', views.listar_professores, name='listar_professores'),
    path('novo', views.cadastrar, name='cadastrar'),
    path('validar_aluno/<int:pk>', views.validar_aluno, name='validar_aluno'),
]

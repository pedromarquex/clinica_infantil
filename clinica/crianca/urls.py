from django.urls import path
from . import views
from exame import views as exame_views

app_name = 'crianca'
urlpatterns = [
    path('todas', views.listar_criancas, name='listar_criancas'),
    path('todas/nova', views.cadastrar, name='cadastrar'),
    path('todas/<int:pk>', views.editar_crianca, name='editar'),
    path('todas/<int:pk>/deletar', views.deletar, name='deletar'),

    # Exames
    path('todas/<int:pk>/exames', exame_views.listar_exames,
         name="listar_exames"),

    # Anamnese
    path('todas/<int:pk>/exames/anamnese/todos',
         exame_views.listar_anamnese, name="listar_anamnese"),
    path('todas/<int:pk>/exames/anamnese/cadastrar',
         exame_views.cadastrar_anamnese, name="cadastrar_anamnese"),
    path('todas/<int:pk>/exames/anamnese/<int:epk>',
         exame_views.editar_anamnese, name="editar_anamnese"),
    path('todas/<int:pk>/exames/anamnese/<int:epk>/deletar',
         exame_views.deletar_anamnese, name="deletar_anamnese"),

    # Exames Clínicos
    path('todas/<int:pk>/exames/clinico_com_dentes/todos',
         exame_views.listar_clinico_com_dentes,
         name="listar_clinico_com_dentes"),
    path('todas/<int:pk>/exames/clinico_com_dentes/cadastrar',
         exame_views.cadastrar_clinico_com_dentes,
         name="cadastrar_clinico_com_dentes"),
    path('todas/<int:pk>/exames/clinico_com_dentes/<int:epk>',
         exame_views.editar_clinico_com_dentes,
         name="editar_clinico_com_dentes"),
    path('todas/<int:pk>/exames/clinico_com_dentes/<int:epk>/deletar',
         exame_views.deletar_clinico_com_dentes,
         name="deletar_clinico_com_dentes"),

    path('todas/<int:pk>/exames/clinico_sem_dentes/todos',
         exame_views.listar_clinico_sem_dentes,
         name="listar_clinico_sem_dentes"),
    path('todas/<int:pk>/exames/clinico_sem_dentes/cadastrar',
         exame_views.cadastrar_clinico_sem_dentes,
         name="cadastrar_clinico_sem_dentes"),
    path('todas/<int:pk>/exames/clinico_sem_dentes/<int:epk>',
         exame_views.editar_clinico_sem_dentes,
         name="editar_clinico_sem_dentes"),
    path('todas/<int:pk>/exames/clinico_sem_dentes/<int:epk>/deletar',
         exame_views.deletar_clinico_sem_dentes,
         name="deletar_clinico_sem_dentes"),

    # Primeiras Consultas
    path('todas/<int:pk>/exames/consulta_com_dentes/todos',
         exame_views.listar_consulta_com_dentes,
         name="listar_consulta_com_dentes"),
    path('todas/<int:pk>/exames/consulta_com_dentes/cadastrar',
         exame_views.cadastrar_consulta_com_dentes,
         name="cadastrar_consulta_com_dentes"),
    path('todas/<int:pk>/exames/consulta_com_dentes/<int:epk>',
         exame_views.editar_consulta_com_dentes,
         name="editar_consulta_com_dentes"),
    path('todas/<int:pk>/exames/consulta_com_dentes/<int:epk>/deletar',
         exame_views.deletar_consulta_com_dentes,
         name="deletar_consulta_com_dentes"),

    path('todas/<int:pk>/exames/consulta_sem_dentes/todos',
         exame_views.listar_consulta_sem_dentes,
         name="listar_consulta_sem_dentes"),
    path('todas/<int:pk>/exames/consulta_sem_dentes/cadastrar',
         exame_views.cadastrar_consulta_sem_dentes,
         name="cadastrar_consulta_sem_dentes"),
    path('todas/<int:pk>/exames/consulta_sem_dentes/<int:epk>',
         exame_views.editar_consulta_sem_dentes,
         name="editar_consulta_sem_dentes"),
    path('todas/<int:pk>/exames/consulta_sem_dentes/<int:epk>/deletar',
         exame_views.deletar_consulta_sem_dentes,
         name="deletar_consulta_sem_dentes"),

    # Retorno
    path('todas/<int:pk>/exames/retorno/todos',
         exame_views.listar_retorno, name="listar_retorno"),
    path('todas/<int:pk>/exames/retorno/cadastrar',
         exame_views.cadastrar_retorno, name="cadastrar_retorno"),
    path('todas/<int:pk>/exames/retorno/<int:epk>',
         exame_views.editar_retorno, name="editar_retorno"),
    path('todas/<int:pk>/exames/retorno/<int:epk>/deletar',
         exame_views.deletar_retorno, name="deletar_retorno"),
]

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Crianca
from aluno.models import Aluno
from professor.models import Professor

from .forms import *
from .models import *
from .filters import *

from datetime import *


@login_required
def cadastrar_anamnese(request, pk):
    crianca = Crianca.objects.get(pk=pk)
    form = AnamneseForm(request.POST)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        anamnese = form

        if anamnese.is_valid():
            anamnese = anamnese.save(commit=False)

            anamnese.user = request.user
            anamnese.crianca = crianca
            anamnese.save()
            return redirect('crianca:listar_exames', pk=crianca.pk)

    return render(request, 'exame/cadastro_anamnese.html',
                  {'user': user, 'crianca': crianca, 'form': form})


@login_required
def editar_anamnese(request, pk, epk):
    c = Crianca.objects.get(pk=pk)
    e = Anamnese.objects.get(pk=epk)
    mensagem_sucesso = None

    form = AnamneseForm(instance=e)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)
    if request.method == "POST":
        exame = AnamneseForm(request.POST, instance=e)

        if exame.is_valid():
            exame = exame.save(commit=False)
            exame.validado_por = None
            exame.data_validacao = None
            exame.valido = False
            exame.save()

        # Criando nova instancia com os dados modificados
        form = AnamneseForm(instance=exame)

        mensagem_sucesso = "Alterações Salvas!"
        return render(request, 'exame/editar_anamnese.html',
                      {'form': form, 'user': user, 'crianca': c,
                       'mensagem_sucesso': mensagem_sucesso, 'exame': e})
    return render(request, 'exame/editar_anamnese.html',
                  {'form': form, 'user': user, 'crianca': c, 'exame': e})


@login_required
def deletar_anamnese(request, pk, epk):
    exame = Anamnese.objects.get(pk=epk)
    exame.delete()

    return redirect('crianca:listar_anamnese', pk=pk)


@login_required
def validar_anamnese(request, pk, epk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('crianca:listar_anamnese', pk=pk)
    e = Anamnese.objects.get(pk=epk)
    if e.valido:
        return redirect('crianca:listar_anamnese', pk=pk)
    e.valido = True
    e.validado_por = request.user
    e.data_validacao = datetime.now()
    e.save()

    return redirect('crianca:listar_anamnese', pk=pk)


@login_required
def cadastrar_clinico_com_dentes(request, pk):
    crianca = Crianca.objects.get(pk=pk)
    form = ClinicoComDentesForm(request.POST)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        clinico = form

        if clinico.is_valid():
            clinico = clinico.save(commit=False)

            clinico.user = request.user
            clinico.crianca = crianca
            clinico.save()
            return redirect('crianca:listar_exames', pk=crianca.pk)

    return render(request, 'exame/cadastro_clinico_com_dentes.html',
                  {'user': user, 'crianca': crianca, 'form': form})


@login_required
def editar_clinico_com_dentes(request, pk, epk):
    c = Crianca.objects.get(pk=pk)
    e = ExameClinicoComDentes.objects.get(pk=epk)
    mensagem_sucesso = None

    form = ClinicoComDentesForm(instance=e)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        exame = ClinicoComDentesForm(request.POST, instance=e)

        if exame.is_valid():
            exame = exame.save(commit=False)
            exame.validado_por = None
            exame.data_validacao = None
            exame.valido = False
            exame.save()

            # Criando nova instancia com os dados modificados
            form = ClinicoComDentesForm(instance=exame)

            mensagem_sucesso = "Alterações Salvas!"
            return render(request, 'exame/editar_clinico_com_dentes.html',
                          {'form': form, 'user': user, 'crianca': c,
                           'mensagem_sucesso': mensagem_sucesso, 'exame': e})

    return render(request, 'exame/editar_clinico_com_dentes.html',
                  {'form': form, 'user': user, 'crianca': c, 'exame': e})


@login_required
def deletar_clinico_com_dentes(request, pk, epk):
    exame = ExameClinicoComDentes.objects.get(pk=epk)
    exame.delete()

    return redirect('crianca:listar_clinico_com_dentes', pk=pk)


@login_required
def validar_clinico_com_dentes(request, pk, epk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('crianca:listar_clinico_com_dentes', pk=pk)
    e = ExameClinicoComDentes.objects.get(pk=epk)
    if e.valido:
        return redirect('crianca:listar_clinico_com_dentes', pk=pk)
    e.valido = True
    e.validado_por = request.user
    e.data_validacao = datetime.now()
    e.save()

    return redirect('crianca:listar_clinico_com_dentes', pk=pk)


@login_required
def cadastrar_clinico_sem_dentes(request, pk):
    crianca = Crianca.objects.get(pk=pk)
    form = ClinicoSemDentesForm(request.POST)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        clinico = form

        if clinico.is_valid():
            clinico = clinico.save(commit=False)

            clinico.user = request.user
            clinico.crianca = crianca
            clinico.save()
            return redirect('crianca:listar_clinico_sem_dentes', pk=crianca.pk)

    return render(request, 'exame/cadastro_clinico_sem_dentes.html',
                  {'user': user, 'crianca': crianca, 'form': form})


@login_required
def editar_clinico_sem_dentes(request, pk, epk):
    c = Crianca.objects.get(pk=pk)
    e = ExameClinicoSemDentes.objects.get(pk=epk)
    mensagem_sucesso = None

    form = ClinicoSemDentesForm(instance=e)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        exame = ClinicoSemDentesForm(request.POST, instance=e)

        if exame.is_valid():
            exame = exame.save(commit=False)
            exame.validado_por = None
            exame.data_validacao = None
            exame.valido = False
            exame.save()

            # Criando nova instancia com os dados modificados
            form = ClinicoSemDentesForm(instance=exame)

            mensagem_sucesso = "Alterações Salvas!"
            return render(request, 'exame/editar_clinico_sem_dentes.html',
                          {'form': form, 'user': user, 'crianca': c,
                           'mensagem_sucesso': mensagem_sucesso, 'exame': e})

    return render(request, 'exame/editar_clinico_sem_dentes.html',
                  {'form': form, 'user': user, 'crianca': c, 'exame': e})


@login_required
def deletar_clinico_sem_dentes(request, pk, epk):
    exame = ExameClinicoSemDentes.objects.get(pk=epk)
    exame.delete()

    return redirect('crianca:listar_clinico_sem_dentes', pk=pk)


@login_required
def validar_clinico_sem_dentes(request, pk, epk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('crianca:listar_clinico_sem_dentes', pk=pk)
    e = ExameClinicoSemDentes.objects.get(pk=epk)
    if e.valido:
        return redirect('crianca:listar_clinico_sem_dentes', pk=pk)
    e.valido = True
    e.validado_por = request.user
    e.data_validacao = datetime.now()
    e.save()

    return redirect('crianca:listar_clinico_sem_dentes', pk=pk)


@login_required
def cadastrar_consulta_com_dentes(request, pk):
    crianca = Crianca.objects.get(pk=pk)
    form = PrimeiraConsultaComDentesForm(request.POST)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        clinico = form

        if clinico.is_valid():
            clinico = clinico.save(commit=False)

            clinico.user = request.user
            clinico.crianca = crianca
            clinico.save()
            return redirect('crianca:listar_consulta_com_dentes',
                            pk=crianca.pk)

    return render(request, 'exame/cadastro_consulta_com_dentes.html',
                  {'user': user, 'crianca': crianca, 'form': form})


@login_required
def editar_consulta_com_dentes(request, pk, epk):
    c = Crianca.objects.get(pk=pk)
    e = PrimeiraConsultaComDentes.objects.get(pk=epk)
    mensagem_sucesso = None

    form = PrimeiraConsultaComDentesForm(instance=e)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        exame = PrimeiraConsultaComDentesForm(request.POST, instance=e)

        if exame.is_valid():
            exame = exame.save(commit=False)
            exame.validado_por = None
            exame.data_validacao = None
            exame.valido = False
            exame.save()

            # Criando nova instancia com os dados modificados
            form = PrimeiraConsultaComDentesForm(instance=exame)

            mensagem_sucesso = "Alterações Salvas!"
            return render(request, 'exame/editar_consulta_com_dentes.html',
                          {'form': form, 'user': user, 'crianca': c,
                           'mensagem_sucesso': mensagem_sucesso, 'exame': e})

    return render(request, 'exame/editar_consulta_com_dentes.html',
                  {'form': form, 'user': user, 'crianca': c, 'exame': e})


@login_required
def deletar_consulta_com_dentes(request, pk, epk):
    exame = PrimeiraConsultaComDentes.objects.get(pk=epk)
    exame.delete()

    return redirect('crianca:listar_consulta_com_dentes', pk=pk)


@login_required
def validar_consulta_com_dentes(request, pk, epk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('crianca:listar_consulta_com_dentes', pk=pk)
    e = PrimeiraConsultaComDentes.objects.get(pk=epk)
    if e.valido:
        return redirect('crianca:listar_consulta_com_dentes', pk=pk)
    e.valido = True
    e.validado_por = request.user
    e.data_validacao = datetime.now()
    e.save()

    return redirect('crianca:listar_consulta_com_dentes', pk=pk)


@login_required
def cadastrar_consulta_sem_dentes(request, pk):
    crianca = Crianca.objects.get(pk=pk)
    form = PrimeiraConsultaSemDentesForm(request.POST)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        clinico = form

        if clinico.is_valid():
            clinico = clinico.save(commit=False)

            clinico.user = request.user
            clinico.crianca = crianca
            clinico.save()
            return redirect('crianca:listar_consulta_sem_dentes',
                            pk=crianca.pk)

    return render(request, 'exame/cadastro_consulta_sem_dentes.html',
                  {'user': user, 'crianca': crianca, 'form': form})


@login_required
def editar_consulta_sem_dentes(request, pk, epk):
    c = Crianca.objects.get(pk=pk)
    e = PrimeiraConsultaSemDentes.objects.get(pk=epk)
    mensagem_sucesso = None

    form = PrimeiraConsultaSemDentesForm(instance=e)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        exame = PrimeiraConsultaSemDentesForm(request.POST, instance=e)

        if exame.is_valid():
            exame = exame.save(commit=False)
            exame.validado_por = None
            exame.data_validacao = None
            exame.valido = False
            exame.save()

            # Criando nova instancia com os dados modificados
            form = PrimeiraConsultaSemDentesForm(instance=exame)

            mensagem_sucesso = "Alterações Salvas!"
            return render(request, 'exame/editar_consulta_sem_dentes.html',
                          {'form': form, 'user': user, 'crianca': c,
                           'mensagem_sucesso': mensagem_sucesso, 'exame': e})

    return render(request, 'exame/editar_consulta_sem_dentes.html',
                  {'form': form, 'user': user, 'crianca': c, 'exame': e})


@login_required
def deletar_consulta_sem_dentes(request, pk, epk):
    exame = PrimeiraConsultaSemDentes.objects.get(pk=epk)
    exame.delete()

    return redirect('crianca:listar_consulta_sem_dentes', pk=pk)


@login_required
def validar_consulta_sem_dentes(request, pk, epk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('crianca:listar_consulta_sem_dentes', pk=pk)
    e = PrimeiraConsultaSemDentes.objects.get(pk=epk)
    if e.valido:
        return redirect('crianca:listar_consulta_sem_dentes', pk=pk)
    e.valido = True
    e.validado_por = request.user
    e.data_validacao = datetime.now()
    e.save()

    return redirect('crianca:listar_consulta_sem_dentes', pk=pk)


@login_required
def cadastrar_retorno(request, pk):
    crianca = Crianca.objects.get(pk=pk)
    form = RetornoForm(request.POST)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        retorno = form

        if retorno.is_valid():
            retorno = retorno.save(commit=False)

            retorno.user = request.user
            retorno.crianca = crianca
            retorno.save()
            return redirect('crianca:listar_exames', pk=crianca.pk)

    return render(request, 'exame/cadastro_retorno.html',
                  {'user': user, 'crianca': crianca, 'form': form})


@login_required
def editar_retorno(request, pk, epk):
    c = Crianca.objects.get(pk=pk)
    e = Retorno.objects.get(pk=epk)
    mensagem_sucesso = None

    form = RetornoForm(instance=e)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        exame = RetornoForm(request.POST, instance=e)

        if exame.is_valid():
            exame = exame.save(commit=False)
            exame.validado_por = None
            exame.data_validacao = None
            exame.valido = False
            exame.save()

            # Criando nova instancia com os dados modificados
            form = RetornoForm(instance=exame)

            mensagem_sucesso = "Alterações Salvas!"
            return render(request, 'exame/editar_retorno.html',
                          {'form': form, 'user': user, 'crianca': c,
                           'mensagem_sucesso': mensagem_sucesso, 'exame': e})

    return render(request, 'exame/editar_retorno.html',
                  {'form': form, 'user': user, 'crianca': c, 'exame': e})


@login_required
def deletar_retorno(request, pk, epk):
    exame = Retorno.objects.get(pk=epk)
    exame.delete()

    return redirect('crianca:listar_retorno', pk=pk)


@login_required
def validar_retorno(request, pk, epk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('crianca:listar_retorno', pk=pk)
    e = Retorno.objects.get(pk=epk)
    if e.valido:
        return redirect('crianca:listar_retorno', pk=pk)
    e.valido = True
    e.validado_por = request.user
    e.data_validacao = datetime.now()
    e.save()

    return redirect('crianca:listar_retorno', pk=pk)


@login_required
def listar_exames(request, pk):
    crianca = Crianca.objects.get(pk=pk)

    try:
        user = Professor.objects.get(user=request.user)
    except Exception:
        user = Aluno.objects.get(user=request.user)

    # Cont para Anamneses
    cont_a = len(Anamnese.objects.filter(crianca=crianca))
    # Cont para Exame Clínico Sem Dentes
    cont_ecsd = len(ExameClinicoSemDentes.objects.filter(crianca=crianca))
    # Cont para Exame Clínico Com Dentes
    cont_eccd = len(ExameClinicoComDentes.objects.filter(crianca=crianca))
    # Cont para Primeira Consulta Com Dentes
    cont_pccd = len(PrimeiraConsultaComDentes.objects.filter(crianca=crianca))
    # Cont para Primeira Consulta Sem Dentes
    cont_pcsd = len(PrimeiraConsultaSemDentes.objects.filter(crianca=crianca))
    # Cont para Retorno
    cont_retorno = len(Retorno.objects.filter(crianca=crianca))

    return render(request, "exame/lista_exames.html",
                  {'user': user, 'crianca': crianca,
                   'cont_a': cont_a,
                   'cont_ecsd': cont_ecsd,
                   'cont_eccd': cont_eccd,
                   'cont_pccd': cont_pccd,
                   'cont_pcsd': cont_pcsd,
                   'cont_retorno': cont_retorno})


@login_required
def listar_anamnese(request, pk):
    is_professor = False
    crianca = Crianca.objects.get(pk=pk)  # pk da criança

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)
        is_professor = True

    anamnese_list = Anamnese.objects.filter(crianca=pk)  # está listando todas as anamenes
    anamnese_filter = AnamneseFilter(request.GET, queryset=anamnese_list)

    return render(request, 'exame/lista_anamnese.html',
                  {'filter': anamnese_filter,
                   'user': user,
                   'crianca': crianca,
                   'is_professor': is_professor})


@login_required
def listar_retorno(request, pk):
    is_professor = False
    crianca = Crianca.objects.get(pk=pk)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)
        is_professor = True

    retorno_list = Retorno.objects.filter(crianca=pk)
    retorno_filter = RetornoFilter(request.GET, queryset=retorno_list)

    return render(request, 'exame/lista_retorno.html',
                  {'filter': retorno_filter,
                   'user': user,
                   'crianca': crianca,
                   'is_professor': is_professor})


@login_required
def listar_clinico_com_dentes(request, pk):
    is_professor = False
    crianca = Crianca.objects.get(pk=pk)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)
        is_professor = True

    clinico_com_dentes_list = ExameClinicoComDentes.objects.filter(crianca=pk)
    clinico_com_dentes_filter = ExameClinicoComDentesFilter(
        request.GET, queryset=clinico_com_dentes_list)

    return render(request, 'exame/lista_clinico_com_dentes.html',
                  {'filter': clinico_com_dentes_filter,
                   'user': user,
                   'crianca': crianca,
                   'is_professor': is_professor})


@login_required
def listar_clinico_sem_dentes(request, pk):
    is_professor = False
    crianca = Crianca.objects.get(pk=pk)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)
        is_professor = True

    clinico_sem_dentes_list = ExameClinicoSemDentes.objects.filter(crianca=pk)
    clinico_sem_dentes_filter = ExameClinicoComDentesFilter(
        request.GET, queryset=clinico_sem_dentes_list)

    return render(request, 'exame/lista_clinico_sem_dentes.html',
                  {'filter': clinico_sem_dentes_filter,
                   'user': user,
                   'crianca': crianca,
                   'is_professor': is_professor})


@login_required
def listar_consulta_com_dentes(request, pk):
    is_professor = False
    crianca = Crianca.objects.get(pk=pk)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)
        is_professor = True

    consulta_com_dentes_list = PrimeiraConsultaComDentes.objects.filter(crianca=pk)
    consulta_com_dentes_filter = ExameClinicoComDentesFilter(
        request.GET, queryset=consulta_com_dentes_list)

    return render(request, 'exame/lista_consulta_com_dentes.html',
                  {'filter': consulta_com_dentes_filter,
                   'user': user,
                   'crianca': crianca,
                   'is_professor': is_professor})


@login_required
def listar_consulta_sem_dentes(request, pk):
    is_professor = False
    crianca = Crianca.objects.get(pk=pk)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)
        is_professor = True

    consulta_sem_dentes_list = PrimeiraConsultaSemDentes.objects.filter(crianca=pk )
    consulta_sem_dentes_filter = ExameClinicoComDentesFilter(
        request.GET, queryset=consulta_sem_dentes_list)

    return render(request, 'exame/lista_consulta_sem_dentes.html',
                  {'filter': consulta_sem_dentes_filter,
                   'user': user,
                   'crianca': crianca,
                   'is_professor': is_professor})

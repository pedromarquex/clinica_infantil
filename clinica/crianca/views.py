from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CriancaForm
from .models import Crianca
from aluno.models import Aluno
from professor.models import Professor
from .filters import CriancaFilter


@login_required
def cadastrar(request):
    form = CriancaForm(request.POST)

    if request.method == "POST":
        crianca = form

        if crianca.is_valid():
            crianca = crianca.save(commit=False)

            crianca.user = request.user
            crianca.save()

            for i in range(1, 22):
                crianca = CriancaForm(request.POST)
                crianca = crianca.save()
                crianca.nome += str(i)
                crianca.save()

            return redirect('crianca:listar_exames')

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    return render(request, 'crianca/cadastro_crianca.html',
                  {'form': form, 'user': user})


@login_required
def listar_criancas(request):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            is_professor = False
        else:
            is_professor = True

    try:
        user = Professor.objects.get(user=request.user)
    except Exception:
        user = Aluno.objects.get(user=request.user)

    crianca_list = Crianca.objects.all()
    crianca_filter = CriancaFilter(request.GET, queryset=crianca_list)

    return render(request, 'crianca/lista_criancas.html',
                  {'filter': crianca_filter,
                   'user': user,
                   'is_professor': is_professor})


@login_required
def editar_crianca(request, pk):
    c = Crianca.objects.get(pk=pk)
    mensagem_sucesso = None

    form = CriancaForm(instance=c)

    try:
        user = Aluno.objects.get(user=request.user)
    except Exception:
        user = Professor.objects.get(user=request.user)

    if request.method == "POST":
        crianca = CriancaForm(request.POST, instance=c)

        if crianca.is_valid():
            crianca = crianca.save()

            # Criando nova instancia com os dados modificados
            form = CriancaForm(instance=crianca)

            mensagem_sucesso = "Alterações Salvas!"
            return render(request, 'crianca/editar_crianca.html',
                          {'form': form, 'user': user, 'crianca': c,
                           'mensagem_sucesso': mensagem_sucesso})

    return render(request, 'crianca/editar_crianca.html',
                  {'form': form, 'user': user, 'crianca': c})


@login_required
def deletar(request, pk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('core:sistema')

    crianca = Crianca.objects.get(pk=pk)
    crianca.delete()

    return redirect('crianca:listar_criancas')

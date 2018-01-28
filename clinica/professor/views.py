from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .forms import ProfessorForm
from .models import Professor
from aluno.models import Aluno
from .filters import ProfessorFilter


@login_required
def editar_perfil(request):
    professor = Professor.objects.get(user=request.user)
    mensagem_sucesso = None
    mensagem_erro = []

    if request.method == "POST":
        form = ProfessorForm(request.POST, request.FILES, instance=professor)

        # Validações de Email, Matrícula e CPF
        try:
            email = request.POST['email']
            if email != professor.email:
                try:
                    Professor.objects.get(email=email)
                    mensagem_erro.append("Este Email já está sendo utilizado.")
                except Exception:
                    pass

                try:
                    Aluno.objects.get(email=email)
                    mensagem_erro.append("Este Email já está sendo utilizado.")
                except Exception:
                    pass

        except Exception:
            pass

        try:
            cpf = request.POST['cpf']

            if cpf != professor.cpf:
                try:
                    Professor.objects.get(cpf=cpf)
                    mensagem_erro.append("Este CPF já está sendo utilizado.")
                except Exception:
                    pass

                try:
                    Aluno.objects.get(cpf=cpf)
                    mensagem_erro.append("Este CPF já está sendo utilizado.")
                except Exception:
                    pass

        except Exception:
            pass

        if len(mensagem_erro) > 0:
            return render(request, 'professor/perfil.html', {
                'user': professor, 'form': form,
                'mensagem_erro': mensagem_erro})

        if form.is_valid():
            professor = form.save()
            professor.user.first_name = professor.nome
            professor.user.email = professor.email
            professor.user.save()
            mensagem_sucesso = "Alterações Salvas!"

            return render(request, 'professor/perfil.html', {
                'user': professor, 'form': form,
                'mensagem_sucesso': mensagem_sucesso})

    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'professor/perfil.html', {
        'user': professor, 'form': form})


@login_required
def listar_professores(request):
    is_professor = False

    try:
        user = Professor.objects.get(user=request.user)
        is_professor = True
    except Exception:
        user = Aluno.objects.get(user=request.user)

    professor_list = Professor.objects.all()
    professor_filter = ProfessorFilter(request.GET, queryset=professor_list)

    return render(request, 'professor/lista_professores.html',
                  {'filter': professor_filter,
                   'user': user,
                   'is_professor': is_professor})


@login_required
def cadastrar(request):

    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('core:sistema')

    form = ProfessorForm(request.POST, request.FILES)
    form_user = UserCreationForm(request.POST)

    # Mensagens de Erro
    erro_singup = []

    if request.method == "POST":
        professor = form
        user = form_user

        if user.is_valid():
            user = user.save()

            # Validações de Email, Matrícula e CPF
            email = request.POST['email']
            try:

                Aluno.objects.get(email=email)
                erro_singup.append("Este Email já está sendo utilizado.")

            except Exception:
                pass

            try:
                Professor.objects.get(email=email)
                erro_singup.append("Este Email já está sendo utilizado.")

            except Exception:
                pass

            cpf = request.POST['cpf']
            try:

                Aluno.objects.get(cpf=cpf)
                erro_singup.append("Este CPF já está sendo utilizado.")

            except Exception:
                pass

            try:
                Professor.objects.get(cpf=cpf)
                erro_singup.append("Este Email já está sendo utilizado.")

            except Exception:
                pass

            if len(erro_singup) > 0:
                user.delete()
                user = Professor.objects.get(user=request.user)
                return render(request, 'professor/cadastro_professor.html',
                              {'form': form,
                               'form_user': form_user,
                               'erro_singup': erro_singup,
                               'user': user
                               })

            if professor.is_valid():
                professor = professor.save(commit=False)

                user.first_name = professor.nome
                user.email = professor.email
                user.is_active = True
                user.save()

                professor.user = user
                professor.save()

                grupo = Group.objects.get(name='Professor')
                grupo.user_set.add(user)

                return redirect('professor:listar_professores')

    user = Professor.objects.get(user=request.user)
    return render(request, 'professor/cadastro_professor.html',
                  {'form': form,
                   'form_user': form_user,
                   'erro_singup': erro_singup,
                   'user': user})


def validar_aluno(request, pk):
    for grupo in request.user.groups.all():
        if grupo.name == "Aluno":
            return redirect('core:sistema')

    aluno = Aluno.objects.get(pk=pk)

    aluno.user.is_active = not aluno.user.is_active
    aluno.user.save()

    return redirect('aluno:listar_alunos')

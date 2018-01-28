from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from aluno.forms import AlunoForm
from aluno.models import Aluno
from professor.models import Professor
from django.core.mail import send_mass_mail


def home(request):
    template_name = "core/index.html"

    form_login = AuthenticationForm()
    form_singup = AlunoForm()
    form_user = UserCreationForm()

    context = {'form_login': form_login,
               'form_singup': form_singup, 'form_user': form_user}

    return render(request, template_name, context)


def login(request):
    erro_login = None
    form_singup = AlunoForm()
    form_login = AuthenticationForm()
    form_user = UserCreationForm()
    context = None
    template_name = "core/index.html"

    if request.method == "POST":
        form_login = AuthenticationForm(request, data=request.POST)

        if form_login.is_valid():
            auth_login(request, form_login.get_user())
            return redirect('core:sistema')
        else:
            erro_login = "Usuário inválido."

    context = {'form_login': form_login,
               'form_singup': form_singup, 'form_user': form_user,
               'erro_login': erro_login}
    return render(request, template_name, context)


def logout(request):
    template_name = "core/index.html"
    form_login = AuthenticationForm()
    form_singup = AlunoForm()
    form_user = UserCreationForm()

    context = {'form_login': form_login,
               'form_singup': form_singup, 'form_user': form_user}

    auth_logout(request)
    return render(request, template_name, context)


def singup(request):
    form_login = AuthenticationForm(request, data=request.POST)
    form_aluno = AlunoForm(request.POST, request.FILES)
    form_user = UserCreationForm(request.POST)

    # Mensagens de Erro e Sucesso
    sucesso_singup = None
    erro_singup = []

    if request.method == "POST":
        aluno = form_aluno
        user = form_user

        if user.is_valid():
            user = user.save()

            # Validações de Email, Matrícula e CPF
            try:
                email = request.POST['email']
                Aluno.objects.get(email=email)
                erro_singup.append("Este Email já está sendo utilizado.")

            except Exception:
                pass

            try:
                cpf = request.POST['cpf']
                Aluno.objects.get(cpf=cpf)
                erro_singup.append("Este CPF já está sendo utilizado.")

            except Exception:
                pass

            try:
                matricula = request.POST['matricula']
                Aluno.objects.get(matricula=matricula)
                erro_singup.append("Esta Matrícula já está sendo utilizado.")

            except Exception:
                pass

            if len(erro_singup) > 0:
                user.delete()
                return render(request, 'core/index.html',
                              {'form_login': form_login,
                               'form_singup': form_aluno,
                               'form_user': form_user,
                               'erro_singup': erro_singup
                               })

            if aluno.is_valid():
                aluno = aluno.save(commit=False)

                user.first_name = aluno.nome
                user.email = aluno.email
                user.is_active = False
                user.save()

                aluno.user = user
                aluno.save()

                grupo = Group.objects.get(name='Aluno')
                grupo.user_set.add(user)

                sucesso_singup = "Usuário cadastrado com sucesso. Aguarde avaliação dos Professores."

                return render(request, 'core/index.html',
                              {'form_login': form_login,
                               'form_singup': form_aluno,
                               'form_user': form_user,
                               'sucesso_singup': sucesso_singup})

    erro_singup.append("Erro ao cadastrar usuário.")
    return render(request, 'core/index.html', {'form_login': form_login,
                                               'form_singup': form_aluno,
                                               'form_user': form_user,
                                               'erro_singup': erro_singup})


@login_required
def sistema(request):
    return redirect('crianca:listar_criancas')

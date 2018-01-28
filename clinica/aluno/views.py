from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AlunoForm
from .models import Aluno
from professor.models import Professor
from .filters import AlunoFilter


@login_required
def editar_perfil(request):
    aluno = Aluno.objects.get(user=request.user)
    mensagem_sucesso = None
    mensagem_erro = []

    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES, instance=aluno)

        # Validações de Email, Matrícula e CPF
        try:
            email = request.POST['email']
            if email != aluno.email:
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

            if cpf != aluno.cpf:
                try:
                    Professor.objects.get(cpf=cpf)
                    mensagem_erro.append("Este Email já está sendo utilizado.")
                except Exception:
                    pass

                try:
                    Aluno.objects.get(cpf=cpf)
                    mensagem_erro.append("Este Email já está sendo utilizado.")
                except Exception:
                    pass

        except Exception:
            pass

        try:
            matricula = request.POST['matricula']

            if matricula != aluno.matricula:
                Aluno.objects.get(matricula=matricula)
                mensagem_erro.append("Esta Matrícula já está sendo utilizado.")

        except Exception:
            pass

        if len(mensagem_erro) > 0:
            return render(request, 'aluno/perfil.html', {
                'user': aluno, 'form': form,
                'mensagem_erro': mensagem_erro})

        if form.is_valid():
            aluno = form.save()
            aluno.user.first_name = aluno.nome
            aluno.user.email = aluno.email
            aluno.user.save()
            mensagem_sucesso = "Alterações Salvas!"

            return render(request, 'aluno/perfil.html', {
                'user': aluno, 'form': form,
                'mensagem_sucesso': mensagem_sucesso})

    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'aluno/perfil.html', {
        'user': aluno, 'form': form})


@login_required
def listar_alunos(request):
    is_professor = False

    try:
        user = Professor.objects.get(user=request.user)
        is_professor = True
    except Exception:
        user = Aluno.objects.get(user=request.user)

    aluno_list = Aluno.objects.all()
    aluno_filter = AlunoFilter(request.GET, queryset=aluno_list)

    return render(request, 'aluno/lista_alunos.html',
                  {'filter': aluno_filter,
                   'user': user,
                   'is_professor': is_professor})

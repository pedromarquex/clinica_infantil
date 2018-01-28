from django.db import models
from django.contrib.auth.models import User
from padroes import choices


class Aluno(models.Model):
    # Dados Pessoais
    nome = models.CharField(max_length=30, null=True)
    cpf = models.CharField(max_length=11, null=True)
    sexo = models.CharField(max_length=10,
                            choices=choices.SEXO_CHOICES, null=True)
    data_nascimento = models.DateField(null=True)
    foto_perfil = models.ImageField(upload_to='perfil', null=True, blank=True)
    # Dados Academicos
    matricula = models.CharField(max_length=11, null=True)
    # Contato
    telefone = models.CharField(max_length=12, null=True)
    email = models.EmailField(null=True)
    # Status
    aprovado = models.BooleanField(default=False, blank=False)
    # User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

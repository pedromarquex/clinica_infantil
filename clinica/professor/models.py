from django.contrib.auth.models import User
from django.db import models
from padroes import choices


class Professor(models.Model):
    # Dados Pessoais
    nome = models.CharField("Nome", max_length=30, null=True)
    cpf = models.CharField("CPF", max_length=11, null=True)
    sexo = models.CharField("Sexo", max_length=12,
                            choices=choices.SEXO_CHOICES, null=True)
    data_nascimento = models.DateField("Data de Nascimento", null=True)
    foto_perfil = models.ImageField(upload_to='perfil', null=True, blank=True)
    # Contato
    telefone = models.CharField("Telefone", max_length=12, null=True)
    email = models.EmailField(null=True)
    # Usuario do Professor
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    class Meta:
        permissions = (
            ('pode_validar', 'Pode validar'), ('can_delete', 'Can Delete'),
        )

    def __str__(self):
        return self.nome

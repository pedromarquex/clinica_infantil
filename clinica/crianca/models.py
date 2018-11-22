# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from padroes.choices import *
from django.utils import timezone


class Crianca(models.Model):
    # Dados Básicos da Criança
    nome = models.CharField(max_length=50, null=True)
    naturalidade = models.CharField(max_length=30, null=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=12, choices=SEXO_CHOICES)

    # Dados Básicos dos Pais
    telefone = models.CharField(max_length=11)
    nome_mae = models.CharField(max_length=30, null=True, blank=True)
    nome_pai = models.CharField(max_length=30, null=True, blank=True)

    # Endereço da Família
    rua = models.CharField(max_length=30, null=True)
    bairro = models.CharField(max_length=30, null=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    cidade = models.CharField(max_length=20, null=True)
    estado = models.CharField(max_length=30, null=True,
                              choices=ESTADO_CHOICES)
    zona = models.CharField(max_length=12, null=True, blank=True,
                            choices=ZONA_CHOICES)

    # Dados Redes Sociais
    facebook = models.CharField(max_length=30, null=True, blank=True)
    instagram = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # Dados Financeiros dos Pais
    renda_familia = models.PositiveIntegerField(null=True)
    numero_pessoas_casa = models.PositiveIntegerField(null=True)
    renda_percapita = models.FloatField(null=True)

    # Dados Acadêmicos dos Pais
    escolaridade_pai = models.CharField(max_length=220,
                                        choices=ESCOLARIDADE_PAIS_CHOICES,
                                        null=True, blank=True)
    escolaridade_mae = models.CharField(max_length=220,
                                        choices=ESCOLARIDADE_PAIS_CHOICES,
                                        null=True, blank=True)

    # Dados Profissionais dos Pais
    profissao_pai = models.CharField(max_length=30, null=True, blank=True)
    profissao_mae = models.CharField(max_length=30, null=True, blank=True)

    # Dados Extras da Criança
    responsavel = models.CharField(
        max_length=30, choices=RESPONSAVEL_CHOICES)
    mora_pais = models.CharField(max_length=10, choices=SIM_NAO_CHOICES)

    nasceu_tempo = models.CharField(
        max_length=40, choices=SIM_NAO_CHOICES)
    nasceu_tempo_meses = models.PositiveIntegerField(
        blank=True, null=True, default=9)
    nasceu_tempo_semanas = models.PositiveIntegerField(
        blank=True, null=True, default=40)
    peso_ao_nascer = models.FloatField(null=True)
    visita_prenatal = models.CharField(max_length=100,
                                       choices=VISITAS_PRENATAL_CHOICES)
    possui_agua_encanada = models.CharField(max_length=10, choices=SIM_NAO_CHOICES, null=True, blank=True)

    # Usuario que cadastou
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    # Data do Cadastro
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nome

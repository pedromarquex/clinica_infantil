from django.db import models
from django.contrib.auth.models import User
from padroes import choices
from crianca.models import Crianca


class Anamnese(models.Model):
    # Alguma Doença na Gravidez?
    doenca_na_gravidez = models.CharField(max_length=3,
                                          choices=choices.SIM_NAO_CHOICES,
                                          null=True)
    # Se sim,
    qual_doenca = models.CharField(max_length=30, null=True, blank=True)

    # Limpa a Boca do Bebê?
    limpa_boca_bebe = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    quem_limpa_boca = models.CharField(max_length=10,
                                       choices=choices.RESPONSAVEL_CHOICES,
                                       null=True, blank=True)
    com_que_limpa = models.CharField(max_length=20, null=True, blank=True)
    quando_comecou = models.CharField(max_length=20, null=True, blank=True)
    quem_orientou = models.CharField(max_length=20, null=True, blank=True)
    horarios = models.CharField(max_length=20, null=True, blank=True)

    # Bebê aceita limpar a boca?
    aceita_limpar = models.CharField(max_length=3,
                                     choices=choices.SIM_NAO_CHOICES,
                                     null=True)
    # Se não,
    quando_nao_aceita = models.CharField(
        max_length=8,
        choices=choices.QUANDO_NAO_ACEITA_CHOICES,
        null=True, blank=True)

    # Tempo, em meses, de amamentação exclusiva
    tempo_amamentacao = models.PositiveIntegerField(default=0, null=True)

    # Ainda mama?
    ainda_mama = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    # Se não,
    quando_parou_mamar = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    idade_peito_noite = models.PositiveIntegerField(
        default=0, null=True, blank=True)

    # Usou mamadeira?
    usou_mamadeira = models.CharField(max_length=3,
                                      choices=choices.SIM_NAO_CHOICES,
                                      null=True)
    # Se sim,
    iniciou_mamadeira = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    deixou_mamadeira = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    idade_usou_durante_sono = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    conteudo_mamadeira = models.CharField(max_length=30, null=True, blank=True)

    # Histórico de Alergias?
    historico_alergias = models.CharField(max_length=3,
                                          choices=choices.SIM_NAO_CHOICES,
                                          null=True)
    # Se sim,
    qual_alergia = models.CharField(max_length=30, null=True, blank=True)

    # Relatar algum problema de saúde?
    relato_problema_saude = models.CharField(max_length=3,
                                             choices=choices.SIM_NAO_CHOICES,
                                             null=True)
    # Se sim,
    qual_problema_saude = models.CharField(
        max_length=30, null=True, blank=True)

    # Histórico de Desordens Sanguíneas?
    historico_desordens_sanguineas = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    qual_desordem_sanguinea = models.CharField(
        max_length=30, null=True, blank=True)

    # Tomando algum medicamento?
    tomando_algum_medicamento = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    qual_medicamento = models.CharField(max_length=30, null=True, blank=True)

    # Exame previamente realizado
    imagem = models.ImageField(upload_to='Anamnese', null=True, blank=True)

    # Usuário que cadastrou
    user = models.ForeignKey(User, related_name='%(class)s_added_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data do Cadastro
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    # É válido
    valido = models.BooleanField(default=False)

    # Usuário que validou
    validado_por = models.ForeignKey(User, related_name='%(class)s_validated_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data de validação
    data_validacao = models.DateTimeField(null=True, blank=True)

    # Crianca
    crianca = models.ForeignKey(
        Crianca, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.data_cadastro)


class PrimeiraConsultaComDentes(models.Model):
    # Amamentação Noturna?
    amamentacao_noturna = models.CharField(max_length=3,
                                           choices=choices.SIM_NAO_CHOICES,
                                           null=True)
    # Se sim,
    mama = models.CharField(max_length=10,
                            choices=choices.MAMA_CHOICES,
                            null=True, blank=True)
    conteudo_mamadeira = models.CharField(max_length=20, null=True, blank=True)
    ingere_guloseimas = models.CharField(max_length=30,
                                         choices=choices.GULOSEIMAS_CHOICES,
                                         null=True, blank=True)

    # Quantas vezes faz HB ao dia?
    hb_ao_dia = models.CharField(max_length=20,
                                 choices=choices.HB_AO_DIA_CHOICES,
                                 null=True)
    horarios_hb = models.CharField(max_length=20, null=True)
    quem_faz_hb = models.CharField(max_length=20,
                                   choices=choices.RESPONSAVEL_CHOICES,
                                   null=True)

    # Aceita Higienizar?
    aceita_higienizar = models.CharField(max_length=3,
                                         choices=choices.SIM_NAO_CHOICES,
                                         null=True)
    # Se não,
    quando_nao_aceita = models.CharField(
        max_length=12,
        choices=choices.QUANDO_NAO_ACEITA_CHOICES,
        null=True, blank=True)

    # Relatar Problema de Saude?
    relato_problema_saude = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    qual_problema_saude = models.CharField(
        max_length=20, null=True, blank=True)

    # Hábitos Bucais não nutritivos?
    habitos_nao_nutritivos = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    quais_habitos = models.CharField(max_length=20, null=True, blank=True)
    frequencia_habitos = models.CharField(max_length=20, null=True, blank=True)
    quando_comecou_habitos = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    permanece_habito = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True, blank=True)
    #     Se não,
    idade_permanceu_habitos = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    problemas_habitos = models.CharField(max_length=20, null=True, blank=True)

    # Com que idade irrompeu o primeiro dente?
    irrompeu_dente = models.CharField(max_length=30,
                                      choices=choices.PRIMEIRO_DENTE_CHOICES,
                                      null=True)
    # Se 'Informar Idade',
    idade_primeiro_dente = models.PositiveIntegerField(
        default=0, null=True, blank=True)

    # Apresentou problema quando os dentes irromperam?
    problema_dentes_irromperam = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES,
        null=True)
    # Se sim,
    quais_problemas = models.CharField(max_length=20, null=True, blank=True)

    # Diário Alimentar últimas 24 horas
    diario_alimentar = models.CharField(max_length=20, null=True)

    # Cáries na Família
    caries_mae = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    caries_pai = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    caries_irmaos = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    classificacao_boca_mae = models.CharField(max_length=16,
                                              choices=choices.SAUDE_BOCA_MAE,
                                              null=True)

    # Por que os dentes ficam cariados?
    motivo_caries = models.CharField(max_length=20, null=True)

    # Já sofreu traumatismos dentários?
    sofreu_traumatismos = models.CharField(max_length=3,
                                           choices=choices.SIM_NAO_CHOICES,
                                           null=True)
    # Se sim,
    trauma = models.CharField(max_length=20, null=True, blank=True)
    lesou_tecido = models.CharField(max_length=3,
                                    choices=choices.SIM_NAO_CHOICES,
                                    null=True, blank=True)
    procurou_dentista = models.CharField(max_length=3,
                                         choices=choices.SIM_NAO_CHOICES,
                                         null=True, blank=True)
    procurou_dentista_tempo = models.PositiveIntegerField(
        default=1, null=True, blank=True)

    # Usuário que cadastrou
    user = models.ForeignKey(User, related_name='%(class)s_added_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data do Cadastro
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    # É válido
    valido = models.BooleanField(default=False)

    # Usuário que validou
    validado_por = models.ForeignKey(User, related_name='%(class)s_validated_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data de validação
    data_validacao = models.DateTimeField(null=True, blank=True)

    # Crianca
    crianca = models.ForeignKey(
        Crianca, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.data_cadastro)


class PrimeiraConsultaSemDentes(models.Model):
    # Hábitos Bucais não nutritivos?
    habitos_nao_nutritivos = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    quais_habitos = models.CharField(max_length=20, null=True, blank=True)
    frequencia_habitos = models.CharField(max_length=20, null=True, blank=True)
    quando_comecou_habitos = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    permanece_habito = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True, blank=True)
    #     Se não,
    idade_permanceu_habitos = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    problemas_habitos = models.CharField(max_length=20, null=True, blank=True)

    # Cáries na Família
    caries_mae = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    caries_pai = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    caries_irmaos = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)
    classificacao_boca_mae = models.CharField(max_length=16,
                                              choices=choices.SAUDE_BOCA_MAE,
                                              null=True)

    # Por que os dentes ficam cariados?
    motivo_caries = models.CharField(max_length=20, null=True)
    como_prevenir = models.CharField(max_length=20, null=True)

    # Examina a boca da Criança?
    examina_boca = models.CharField(max_length=3,
                                    choices=choices.SIM_NAO_CHOICES,
                                    null=True)
    # Usuário que cadastrou
    user = models.ForeignKey(User, related_name='%(class)s_added_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data do Cadastro
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    # É válido
    valido = models.BooleanField(default=False)

    # Usuário que validou
    validado_por = models.ForeignKey(User, related_name='%(class)s_validated_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data de validação
    data_validacao = models.DateTimeField(null=True, blank=True)

    # Crianca
    crianca = models.ForeignKey(
        Crianca, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.data_cadastro)


class ExameClinicoSemDentes(models.Model):
    # Língua suja?
    lingua_suja = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES, null=True)

    # Tecidos moles
    tecido_mole = models.CharField(
        max_length=12,
        choices=choices.TECIDO_MOLE_CHOICES, null=True)
    # Se 'Alterado',
    tecido_alterado = models.CharField(max_length=20, null=True, blank=True)

    # Tipo de Língua
    lingua = models.CharField(
        max_length=12,
        choices=choices.LINGUA_CHOICES, null=True)
    # Se 'Outro',
    tipo_lingua = models.CharField(max_length=20, null=True, blank=True)

    # Anquiloglossia
    anquiloglossia = models.CharField(
        max_length=12,
        choices=choices.ANQUILOGLOSSIA_CHOICES, null=True)

    # Usuário que cadastrou
    user = models.ForeignKey(User, related_name='%(class)s_added_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data do Cadastro
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    # É válido
    valido = models.BooleanField(default=False)

    # Usuário que validou
    validado_por = models.ForeignKey(User, related_name='%(class)s_validated_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data de validação
    data_validacao = models.DateTimeField(null=True, blank=True)

    # Crianca
    crianca = models.ForeignKey(
        Crianca, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.data_cadastro)


class ExameClinicoComDentes(models.Model):
    # Placa visível?
    placa = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)

    # Língua suja?
    lingua_suja = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)

    # Sangramento após escovação?
    sangramento_escovacao = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)

    # Tecidos moles?
    tecidos_moles = models.CharField(
        max_length=20, choices=choices.TECIDO_MOLE_CHOICES)
    # Se 'Alterado',
    tecidos_moles_alteracao = models.CharField(
        blank=True, max_length=100, )

    # Tipo de Língua
    lingua = models.CharField(
        max_length=15, choices=choices.LINGUA_CHOICES)
    # Se 'Outro',
    lingua_tipo = models.CharField(
        null=True, blank=True, max_length=30, )

    # Anquiloglossia
    anquiloglossia = models.CharField(
        max_length=30, choices=choices.ANQUILOGLOSSIA_CHOICES)

    # Dentição Completa?
    denticao_completa = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES)
    # Se sim,
    arco_superior = models.CharField(
        max_length=30, choices=choices.TIPOARCO_CHOICES, blank=True)
    arco_inferior = models.CharField(
        max_length=30, choices=choices.TIPOARCO_CHOICES, blank=True)

    # Somente quando 'Dentição Completa'
    diastema_primata_superior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    diastema_primata_inferior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    mordida_cruzada_posterior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    mordida_cruzada_anterior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    mordida_aberta_anterior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    relacao_canina_direita = models.CharField(
        max_length=15, choices=choices.CLASSE_CHOICES, blank=True)
    relacao_canina_esquerda = models.CharField(
        max_length=15, choices=choices.CLASSE_CHOICES, blank=True)

    # Condicao Dentaria Inicial
    dente_55 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_54 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_53 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_52 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_51 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    dente_65 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_64 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_63 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_62 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_61 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    dente_85 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_84 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_83 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_82 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_81 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    dente_75 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_74 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_73 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_72 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_71 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    # Procedimentos realizados
    consulta = models.BooleanField(
        blank=True, default=False)
    atividade_educativa = models.BooleanField(
        blank=True, default=False)
    aplicacao_fluor = models.BooleanField(
        blank=True, default=False)
    art = models.BooleanField(blank=True, default=False)
    art_opcao = models.CharField(
        max_length=20, blank=True, null=True)
    frenotomia = models.BooleanField(
        blank=True, default=False)
    enc_tratamento_odonto = models.BooleanField(
        blank=True, default=False)
    enc_UFPI_idade = models.BooleanField(
        blank=True, default=False)

    # Observações e Planejamento
    observacoes = models.CharField(
        max_length=100, blank=True)
    planejamento = models.CharField(
        max_length=100, blank=True)

    # Anexo
    imagem = models.ImageField(
        upload_to='ExameComDentes', blank=True, null=True)

    # Usuário que cadastrou
    user = models.ForeignKey(User, related_name='%(class)s_added_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data do Cadastro
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    # É válido
    valido = models.BooleanField(default=False)

    # Usuário que validou
    validado_por = models.ForeignKey(User, related_name='%(class)s_validated_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data de validação
    data_validacao = models.DateTimeField(null=True, blank=True)

    # Crianca
    crianca = models.ForeignKey(
        Crianca, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.data_cadastro)


class Retorno(models.Model):
    # Amamentação Noturna?
    amamentacao_noturna = models.CharField(max_length=3,
                                           choices=choices.SIM_NAO_CHOICES,
                                           null=True)
    # Se sim,
    mama = models.CharField(max_length=10,
                            choices=choices.MAMA_CHOICES,
                            null=True, blank=True)
    conteudo_mamadeira = models.CharField(max_length=20, null=True, blank=True)
    ingere_guloseimas = models.CharField(max_length=30,
                                         choices=choices.GULOSEIMAS_CHOICES,
                                         null=True, blank=True)

    # Quantas vezes faz HB ao dia?
    hb_ao_dia = models.CharField(max_length=20,
                                 choices=choices.HB_AO_DIA_CHOICES,
                                 null=True)
    horarios_hb = models.CharField(max_length=20, null=True)
    quem_faz_hb = models.CharField(max_length=20,
                                   choices=choices.RESPONSAVEL_CHOICES,
                                   null=True)

    # Aceita Higienizar?
    aceita_higienizar = models.CharField(max_length=3,
                                         choices=choices.SIM_NAO_CHOICES,
                                         null=True)
    # Se não,
    quando_nao_aceita = models.CharField(
        max_length=12,
        choices=choices.QUANDO_NAO_ACEITA_CHOICES,
        null=True, blank=True)

    # Hábitos Bucais não nutritivos?
    habitos_nao_nutritivos = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    quais_habitos = models.CharField(max_length=20, null=True, blank=True)
    frequencia_habitos = models.CharField(max_length=20, null=True, blank=True)
    quando_comecou_habitos = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    permanece_habito = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True, blank=True)
    #     Se não,
    idade_permanceu_habitos = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    problemas_habitos = models.CharField(max_length=20, null=True, blank=True)

    # Diário Alimentar
    diario_alimentar = models.CharField(
        max_length=35, null=True, choices=choices.DIARIO_ALIMENTAR_CHOICES)

    # Relatar algum problema de saúde?
    relato_problema_saude = models.CharField(max_length=3,
                                             choices=choices.SIM_NAO_CHOICES,
                                             null=True)
    # Se sim,
    qual_problema_saude = models.CharField(
        max_length=30, null=True, blank=True)

    # Tomando algum medicamento?
    tomando_algum_medicamento = models.CharField(
        max_length=3,
        choices=choices.SIM_NAO_CHOICES, null=True)
    # Se sim,
    qual_medicamento = models.CharField(max_length=30, null=True, blank=True)

    # Exame Clínico Com Dentes
    # Placa visível?
    placa = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)

    # Língua suja?
    lingua_suja = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)

    # Sangramento após escovação?
    sangramento_escovacao = models.CharField(
        max_length=3, choices=choices.SIM_NAO_CHOICES, null=True)

    # Tecidos moles?
    tecidos_moles = models.CharField(
        max_length=20, choices=choices.TECIDO_MOLE_CHOICES)
    # Se 'Alterado',
    tecidos_moles_alteracao = models.CharField(
        blank=True, max_length=100, )

    # Tipo de Língua
    lingua = models.CharField(
        max_length=15, choices=choices.LINGUA_CHOICES)
    # Se 'Outro',
    lingua_tipo = models.CharField(
        null=True, blank=True, max_length=30, )

    # Anquiloglossia
    anquiloglossia = models.CharField(
        max_length=30, choices=choices.ANQUILOGLOSSIA_CHOICES)

    # Dentição Completa?
    denticao_completa = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES)
    # Se sim,
    arco_superior = models.CharField(
        max_length=30, choices=choices.TIPOARCO_CHOICES, blank=True)
    arco_inferior = models.CharField(
        max_length=30, choices=choices.TIPOARCO_CHOICES, blank=True)

    # Somente quando 'Dentição Completa'
    diastema_primata_superior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    diastema_primata_inferior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    mordida_cruzada_posterior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    mordida_cruzada_anterior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    mordida_aberta_anterior = models.CharField(
        max_length=4, choices=choices.SIM_NAO_CHOICES, blank=True)
    relacao_canina_direita = models.CharField(
        max_length=15, choices=choices.CLASSE_CHOICES, blank=True)
    relacao_canina_esquerda = models.CharField(
        max_length=15, choices=choices.CLASSE_CHOICES, blank=True)

    # Condicao Dentaria Inicial
    dente_55 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_54 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_53 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_52 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_51 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    dente_65 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_64 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_63 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_62 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_61 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    dente_85 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_84 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_83 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_82 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_81 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    dente_75 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_74 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_73 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_72 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)
    dente_71 = models.CharField(null=True, blank=True, max_length=5,
                                choices=choices.CONDICAO_DENTARIA_CHOICES)

    # Procedimentos realizados
    consulta = models.BooleanField(
        blank=True, default=False)
    atividade_educativa = models.BooleanField(
        blank=True, default=False)
    aplicacao_fluor = models.BooleanField(
        blank=True, default=False)
    art = models.BooleanField(blank=True, default=False)
    art_opcao = models.CharField(
        max_length=20, blank=True, null=True)
    frenotomia = models.BooleanField(
        blank=True, default=False)
    enc_tratamento_odonto = models.BooleanField(
        blank=True, default=False)
    enc_UFPI_idade = models.BooleanField(
        blank=True, default=False)

    # Observações e Planejamento
    observacoes = models.CharField(
        max_length=100, blank=True)
    planejamento = models.CharField(
        max_length=100, blank=True)

    # Anexo
    imagem = models.ImageField(
        upload_to='ExameRetorno', blank=True, null=True)

    # Usuário que cadastrou
    user = models.ForeignKey(User, related_name='%(class)s_added_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data do Cadastro
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    # É válido
    valido = models.BooleanField(default=False)

    # Usuário que validou
    validado_por = models.ForeignKey(User, related_name='%(class)s_validated_by', on_delete=models.CASCADE, null=True, blank=True)

    # Data de validação
    data_validacao = models.DateTimeField(null=True, blank=True)

    # Crianca
    crianca = models.ForeignKey(
        Crianca, on_delete=models.CASCADE, null=True, blank=True)

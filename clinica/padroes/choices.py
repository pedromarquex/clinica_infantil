SIM_NAO_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

SEXO_CHOICES = (
    ('Feminino', 'Feminino'),
    ('Masculino', 'Masculino')
)


MORA_PAIS_CHOICES = (
    ('Sim', 'Sim'),
    ('Nao', 'Nao'),
)

ESCOLARIDADE_PAIS_CHOICES = (
    ('Primario Incompleto', 'Primário Incompleto'),
    ('Primario Completo', 'Primário Completo'),
    ('Ginasio Incompleto', 'Ginásio Incompleto'),
    ('Ginasio Completo', 'Ginásio Completo'),
    ('2 Grau Incompleto AcadEmico', '2º Grau Incompleto Acadêmico'),
    ('2 Grau Completo Academico', '2º Grau Completo Acadêmico'),
    ('2 Grau Incompleto Tecnico', '2º Grau Incompleto Técnico'),
    ('2 Grau Completo Tecnico', '2º Grau Completo Técnico'),
    ('3 Grau Incompleto', '3º Grau Incompleto'),
    ('3 Grau Completo', '3º Grau Completo'),
    ('Pos Graduacao ou Especializacao Cursando', 'Pós Grad./Espec. Cursando'),
    ('Pos Graduacao ou Especializacao Concluido',
        'Pós Grad./Espec. Concluído'),
    ('Mestrado Cursando', 'Mestrado Cursando'),
    ('Mestrado Concluido', 'Mestrado Concluído'),
    ('Doutorado Cursando', 'Doutorado Cursando'),
    ('Doutorado Concluido', 'Doutorado Concluído'),
    ('MBA Cursando', 'MBA Cursando'),
    ('MBA ConcluIdo', 'MBA Concluído'),
)

FREQUENTOU_CHOICES = (
    ('Sim', 'Sim'),
    ('Nao', 'Nao'),
    ('Pegou encaminhamento', 'Pegou encaminhamento')
)

NASCEU_TEMPO_CHOICES = (
    ('1', 'menor que 2.500'),
    ('2', 'entre 2.500 e 3000'),
    ('3', 'entre 3.000 e 3.500'),
    ('4', 'entre 3.500 e 4.500'),
    ('5', 'maior que 4.500'),
    ('6', 'Não Lembra'),
)

PESO_AO_NASCER_CHOICES = (
    ('Menor que 2.500', 'Menor que 2.500'),
    ('Entre 2.500 e 3000', 'Entre 2.500 e 3000'),
    ('Entre 3.000 e 3.500', 'Entre 3.000 e 3.500'),
    ('Mais que 4.500', 'Mais que 4.500'),
    ('Nao Lembra', ' Não Lembra'),
)

VISITAS_PRENATAL_CHOICES = (
    ('0', 'Nao fez/Nao Lembra'),
    ('1 a 3', 'De 1 a 3 visitas'),
    ('4 a 6', 'De 4 a 6 visitas'),
    ('7 a 9', 'De 7 a 9 visitas'),
    ('Mais de 9', 'Mais de 9 visitas')
)

RESPONSAVEL_CHOICES = (
    ('Mae', 'Mãe'),
    ('Pai', 'Pai'),
    ('Avos', 'Avós'),
    ('Outro Parente', 'Outro parente'),
    ('Baba', 'Babá'),
    ('Outra pessoa', 'Outra pessoa')
)

ESTADO_CHOICES = (
    ('Acre', 'Acre'),
    ('Alagoas', 'Alagoas'),
    ('Amapa', 'Amapa'),
    ('Amazonas', 'Amazonas'),
    ('Bahia', 'Bahia'),
    ('Ceara', 'Ceara'),
    ('Distrito Federal', 'Distrito Federal'),
    ('Espirito Santo', 'Espirito Santo'),
    ('Goias', 'Goias'),
    ('Maranhao', 'Maranhao'),
    ('Mato Grosso', 'Mato Grosso'),
    ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
    ('Minas Gerais', 'Minas Gerais'),
    ('Para', 'Para'),
    ('Paraiba', 'Paraiba'),
    ('Parana', 'Parana'),
    ('Pernambuco', 'Pernambuco'),
    ('Piaui', 'Piaui'),
    ('Rio de Janeiro', 'Rio de Janeiro'),
    ('Rio Grande do Norte', 'Rio Grande do Norte'),
    ('Rio Grande do Sul', 'Rio Grande do Sul'),
    ('Rondonia', 'Rondonia'),
    ('Roraima', 'Roraima'),
    ('Santa Catarina', 'Santa Catarina'),
    ('Sao Paulo', 'Sao Paulo'),
    ('Sergipe', 'Sergipe'),
    ('Tocantins', 'Tocantins')
)

ZONA_CHOICES = (
    ('Zona Norte', 'Norte'),
    ('Zona Leste', 'Leste'),
    ('Zona Sul', 'Sul'),
    ('Zona Sudeste', 'Sudeste'),
    ('Centro', 'Centro')
)


QUANDO_NAO_ACEITA_CHOICES = {
    ('Insiste', 'Insiste'),
    ('Dessite', 'Desiste')
}

MAMA_CHOICES = {
    ('Mamadeira', 'Mamadeira'),
    ('Peito', 'Peito')
}

GULOSEIMAS_CHOICES = {
    ('Livremente', 'Livremente'),
    ('Três vezes por Semana', 'Até três vezes por Semana'),
    ('Raramente', 'Raramente'),
    ('Nunca', 'Nunca')
}

HB_AO_DIA_CHOICES = {
    ('Uma vez ao dia', 'Uma vez ao dia'),
    ('Duas vezes ao dia', 'Duas vezes ao dia'),
    ('Três vezes ao dia', 'Três vezes ao dia'),
    ('Quatro vezes ao dia', 'Quatro vezes ao dia'),
    ('Mais de quatro vezes ao dia', 'Mais de quatro vezes ao dia')
}

PRIMEIRO_DENTE_CHOICES = {
    ('Nasceu com dente', 'Nasceu com dente'),
    ('Nao lembra', 'Nao lembra'),
    ('Informar Idade', 'Informar Idade')
}

DIARIO_ALIMENTAR_CHOICES = {
    ('Menos de 6 ingestoes de acucar', 'Menos de 6 ingestões de açucar por dia'),
    ('Mais de 6 ingestoes de acucar', 'Mais de 6 ingestoes de açucar por dia')
}

SAUDE_BOCA_MAE = {
    ('Boa', 'Boa'),
    ('Regular', 'Regular'),
    ('Ruim', 'Ruim'),
    ('Mae nao presente', 'Mae nao esta presente')
}

TECIDO_MOLE_CHOICES = {
    ('Normal', 'Normal'),
    ('Alterado', 'Alterado')
}

LINGUA_CHOICES = {
    ('Normal', 'Normal'),
    ('Geografica', 'Geográfica'),
    ('Sulcada', 'Sulcada'),
    ('Outro', 'Outro')
}

ANQUILOGLOSSIA_CHOICES = {
    ('Sim', 'Sim'),
    ('Nao', 'Não'),
    ('Inconclusivo', 'Inconclusivo'),
    ('Nao permitiu Avaliar', 'Não permitiu Avaliar')
}

CONDICAO_DENTARIA_CHOICES = {
    ("A", "A"),
    ("MB", "MB"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
    ("G", "G"),
    ("K", "K"),
    ("T", "T"),
    ("MB", "MB"),
}

CLASSE_CHOICES = (
    ('Classe I', 'Classe I'),
    ('Classe II', 'Classe II'),
    ('Classe III', 'Classe III'),
)

TIPOARCO_CHOICES = (
    ('Tipo I', 'Tipo I'),
    ('Tipo II', 'Tipo II'),
)

# Generated by Django 2.1.2 on 2018-10-19 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crianca', '0002_auto_20181019_0149'),
        ('exame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExameClinicoComDentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('lingua_suja', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('sangramento_escovacao', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('tecidos_moles', models.CharField(choices=[('Alterado', 'Alterado'), ('Normal', 'Normal')], max_length=20)),
                ('tecidos_moles_alteracao', models.CharField(blank=True, max_length=100)),
                ('lingua', models.CharField(choices=[('Geografica', 'Geográfica'), ('Sulcada', 'Sulcada'), ('Outro', 'Outro'), ('Normal', 'Normal')], max_length=15)),
                ('lingua_tipo', models.CharField(blank=True, max_length=30, null=True)),
                ('anquiloglossia', models.CharField(choices=[('Nao permitiu Avaliar', 'Não permitiu Avaliar'), ('Sim', 'Sim'), ('Nao', 'Não'), ('Inconclusivo', 'Inconclusivo')], max_length=30)),
                ('denticao_completa', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('arco_superior', models.CharField(blank=True, choices=[('Tipo I', 'Tipo I'), ('Tipo II', 'Tipo II')], max_length=30)),
                ('arco_inferior', models.CharField(blank=True, choices=[('Tipo I', 'Tipo I'), ('Tipo II', 'Tipo II')], max_length=30)),
                ('diastema_primata_superior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('diastema_primata_inferior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('mordida_cruzada_posterior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('mordida_cruzada_anterior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('mordida_aberta_anterior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('relacao_canina_direita', models.CharField(blank=True, choices=[('Classe I', 'Classe I'), ('Classe II', 'Classe II'), ('Classe III', 'Classe III')], max_length=15)),
                ('relacao_canina_esquerda', models.CharField(blank=True, choices=[('Classe I', 'Classe I'), ('Classe II', 'Classe II'), ('Classe III', 'Classe III')], max_length=15)),
                ('dente_55', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_54', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_53', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_52', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_51', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_65', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_64', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_63', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_62', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_61', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_85', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_84', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_83', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_82', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_81', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_75', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_74', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_73', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_72', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_71', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('consulta', models.BooleanField(blank=True, default=False)),
                ('atividade_educativa', models.BooleanField(blank=True, default=False)),
                ('aplicacao_fluor', models.BooleanField(blank=True, default=False)),
                ('art', models.BooleanField(blank=True, default=False)),
                ('art_opcao', models.CharField(blank=True, max_length=20, null=True)),
                ('frenotomia', models.BooleanField(blank=True, default=False)),
                ('enc_tratamento_odonto', models.BooleanField(blank=True, default=False)),
                ('enc_UFPI_idade', models.BooleanField(blank=True, default=False)),
                ('observacoes', models.CharField(blank=True, max_length=100)),
                ('planejamento', models.CharField(blank=True, max_length=100)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='ExameComDentes')),
                ('data_cadastro', models.DateField(auto_now_add=True, null=True)),
                ('valido', models.BooleanField(default=False)),
                ('data_validacao', models.DateTimeField(blank=True, null=True)),
                ('crianca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crianca.Crianca')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exameclinicocomdentes_added_by', to=settings.AUTH_USER_MODEL)),
                ('validado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exameclinicocomdentes_validated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExameClinicoSemDentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lingua_suja', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('tecido_mole', models.CharField(choices=[('Alterado', 'Alterado'), ('Normal', 'Normal')], max_length=12, null=True)),
                ('tecido_alterado', models.CharField(blank=True, max_length=20, null=True)),
                ('lingua', models.CharField(choices=[('Geografica', 'Geográfica'), ('Sulcada', 'Sulcada'), ('Outro', 'Outro'), ('Normal', 'Normal')], max_length=12, null=True)),
                ('tipo_lingua', models.CharField(blank=True, max_length=20, null=True)),
                ('anquiloglossia', models.CharField(choices=[('Nao permitiu Avaliar', 'Não permitiu Avaliar'), ('Sim', 'Sim'), ('Nao', 'Não'), ('Inconclusivo', 'Inconclusivo')], max_length=12, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, null=True)),
                ('valido', models.BooleanField(default=False)),
                ('data_validacao', models.DateTimeField(blank=True, null=True)),
                ('crianca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crianca.Crianca')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exameclinicosemdentes_added_by', to=settings.AUTH_USER_MODEL)),
                ('validado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exameclinicosemdentes_validated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrimeiraConsultaComDentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amamentacao_noturna', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('mama', models.CharField(blank=True, choices=[('Peito', 'Peito'), ('Mamadeira', 'Mamadeira')], max_length=10, null=True)),
                ('conteudo_mamadeira', models.CharField(blank=True, max_length=20, null=True)),
                ('ingere_guloseimas', models.CharField(blank=True, choices=[('Três vezes por Semana', 'Até três vezes por Semana'), ('Livremente', 'Livremente'), ('Raramente', 'Raramente'), ('Nunca', 'Nunca')], max_length=30, null=True)),
                ('hb_ao_dia', models.CharField(choices=[('Uma vez ao dia', 'Uma vez ao dia'), ('Mais de quatro vezes ao dia', 'Mais de quatro vezes ao dia'), ('Quatro vezes ao dia', 'Quatro vezes ao dia'), ('Três vezes ao dia', 'Três vezes ao dia'), ('Duas vezes ao dia', 'Duas vezes ao dia')], max_length=20, null=True)),
                ('horarios_hb', models.CharField(max_length=20, null=True)),
                ('quem_faz_hb', models.CharField(choices=[('Mae', 'Mãe'), ('Pai', 'Pai'), ('Avos', 'Avós'), ('Outro Parente', 'Outro parente'), ('Baba', 'Babá'), ('Outra pessoa', 'Outra pessoa')], max_length=20, null=True)),
                ('aceita_higienizar', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('quando_nao_aceita', models.CharField(blank=True, choices=[('Dessite', 'Desiste'), ('Insiste', 'Insiste')], max_length=12, null=True)),
                ('relato_problema_saude', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('qual_problema_saude', models.CharField(blank=True, max_length=20, null=True)),
                ('habitos_nao_nutritivos', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('quais_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('frequencia_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('quando_comecou_habitos', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('permanece_habito', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('idade_permanceu_habitos', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('problemas_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('irrompeu_dente', models.CharField(choices=[('Nasceu com dente', 'Nasceu com dente'), ('Nao lembra', 'Nao lembra'), ('Informar Idade', 'Informar Idade')], max_length=30, null=True)),
                ('idade_primeiro_dente', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('problema_dentes_irromperam', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('quais_problemas', models.CharField(blank=True, max_length=20, null=True)),
                ('diario_alimentar', models.CharField(max_length=20, null=True)),
                ('caries_mae', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('caries_pai', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('caries_irmaos', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('classificacao_boca_mae', models.CharField(choices=[('Ruim', 'Ruim'), ('Regular', 'Regular'), ('Mae nao presente', 'Mae nao esta presente'), ('Boa', 'Boa')], max_length=16, null=True)),
                ('motivo_caries', models.CharField(max_length=20, null=True)),
                ('sofreu_traumatismos', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('trauma', models.CharField(blank=True, max_length=20, null=True)),
                ('lesou_tecido', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('procurou_dentista', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('procurou_dentista_tempo', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, null=True)),
                ('valido', models.BooleanField(default=False)),
                ('data_validacao', models.DateTimeField(blank=True, null=True)),
                ('crianca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crianca.Crianca')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primeiraconsultacomdentes_added_by', to=settings.AUTH_USER_MODEL)),
                ('validado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primeiraconsultacomdentes_validated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrimeiraConsultaSemDentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitos_nao_nutritivos', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('quais_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('frequencia_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('quando_comecou_habitos', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('permanece_habito', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('idade_permanceu_habitos', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('problemas_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('caries_mae', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('caries_pai', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('caries_irmaos', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('classificacao_boca_mae', models.CharField(choices=[('Ruim', 'Ruim'), ('Regular', 'Regular'), ('Mae nao presente', 'Mae nao esta presente'), ('Boa', 'Boa')], max_length=16, null=True)),
                ('motivo_caries', models.CharField(max_length=20, null=True)),
                ('como_prevenir', models.CharField(max_length=20, null=True)),
                ('examina_boca', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, null=True)),
                ('valido', models.BooleanField(default=False)),
                ('data_validacao', models.DateTimeField(blank=True, null=True)),
                ('crianca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crianca.Crianca')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primeiraconsultasemdentes_added_by', to=settings.AUTH_USER_MODEL)),
                ('validado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primeiraconsultasemdentes_validated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Retorno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amamentacao_noturna', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('mama', models.CharField(blank=True, choices=[('Peito', 'Peito'), ('Mamadeira', 'Mamadeira')], max_length=10, null=True)),
                ('conteudo_mamadeira', models.CharField(blank=True, max_length=20, null=True)),
                ('ingere_guloseimas', models.CharField(blank=True, choices=[('Três vezes por Semana', 'Até três vezes por Semana'), ('Livremente', 'Livremente'), ('Raramente', 'Raramente'), ('Nunca', 'Nunca')], max_length=30, null=True)),
                ('hb_ao_dia', models.CharField(choices=[('Uma vez ao dia', 'Uma vez ao dia'), ('Mais de quatro vezes ao dia', 'Mais de quatro vezes ao dia'), ('Quatro vezes ao dia', 'Quatro vezes ao dia'), ('Três vezes ao dia', 'Três vezes ao dia'), ('Duas vezes ao dia', 'Duas vezes ao dia')], max_length=20, null=True)),
                ('horarios_hb', models.CharField(max_length=20, null=True)),
                ('quem_faz_hb', models.CharField(choices=[('Mae', 'Mãe'), ('Pai', 'Pai'), ('Avos', 'Avós'), ('Outro Parente', 'Outro parente'), ('Baba', 'Babá'), ('Outra pessoa', 'Outra pessoa')], max_length=20, null=True)),
                ('aceita_higienizar', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('quando_nao_aceita', models.CharField(blank=True, choices=[('Dessite', 'Desiste'), ('Insiste', 'Insiste')], max_length=12, null=True)),
                ('habitos_nao_nutritivos', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('quais_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('frequencia_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('quando_comecou_habitos', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('permanece_habito', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('idade_permanceu_habitos', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('problemas_habitos', models.CharField(blank=True, max_length=20, null=True)),
                ('diario_alimentar', models.CharField(choices=[('Menos de 6 ingestoes de acucar', 'Menos de 6 ingestões de açucar por dia'), ('Mais de 6 ingestoes de acucar', 'Mais de 6 ingestoes de açucar por dia')], max_length=35, null=True)),
                ('relato_problema_saude', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('qual_problema_saude', models.CharField(blank=True, max_length=30, null=True)),
                ('tomando_algum_medicamento', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('qual_medicamento', models.CharField(blank=True, max_length=30, null=True)),
                ('placa', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('lingua_suja', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('sangramento_escovacao', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True)),
                ('tecidos_moles', models.CharField(choices=[('Alterado', 'Alterado'), ('Normal', 'Normal')], max_length=20)),
                ('tecidos_moles_alteracao', models.CharField(blank=True, max_length=100)),
                ('lingua', models.CharField(choices=[('Geografica', 'Geográfica'), ('Sulcada', 'Sulcada'), ('Outro', 'Outro'), ('Normal', 'Normal')], max_length=15)),
                ('lingua_tipo', models.CharField(blank=True, max_length=30, null=True)),
                ('anquiloglossia', models.CharField(choices=[('Nao permitiu Avaliar', 'Não permitiu Avaliar'), ('Sim', 'Sim'), ('Nao', 'Não'), ('Inconclusivo', 'Inconclusivo')], max_length=30)),
                ('denticao_completa', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('arco_superior', models.CharField(blank=True, choices=[('Tipo I', 'Tipo I'), ('Tipo II', 'Tipo II')], max_length=30)),
                ('arco_inferior', models.CharField(blank=True, choices=[('Tipo I', 'Tipo I'), ('Tipo II', 'Tipo II')], max_length=30)),
                ('diastema_primata_superior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('diastema_primata_inferior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('mordida_cruzada_posterior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('mordida_cruzada_anterior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('mordida_aberta_anterior', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=4)),
                ('relacao_canina_direita', models.CharField(blank=True, choices=[('Classe I', 'Classe I'), ('Classe II', 'Classe II'), ('Classe III', 'Classe III')], max_length=15)),
                ('relacao_canina_esquerda', models.CharField(blank=True, choices=[('Classe I', 'Classe I'), ('Classe II', 'Classe II'), ('Classe III', 'Classe III')], max_length=15)),
                ('dente_55', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_54', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_53', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_52', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_51', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_65', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_64', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_63', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_62', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_61', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_85', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_84', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_83', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_82', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_81', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_75', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_74', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_73', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_72', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('dente_71', models.CharField(blank=True, choices=[('C', 'C'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('D', 'D'), ('A', 'A'), ('MB', 'MB'), ('K', 'K'), ('T', 'T'), ('B', 'B')], max_length=5, null=True)),
                ('consulta', models.BooleanField(blank=True, default=False)),
                ('atividade_educativa', models.BooleanField(blank=True, default=False)),
                ('aplicacao_fluor', models.BooleanField(blank=True, default=False)),
                ('art', models.BooleanField(blank=True, default=False)),
                ('art_opcao', models.CharField(blank=True, max_length=20, null=True)),
                ('frenotomia', models.BooleanField(blank=True, default=False)),
                ('enc_tratamento_odonto', models.BooleanField(blank=True, default=False)),
                ('enc_UFPI_idade', models.BooleanField(blank=True, default=False)),
                ('observacoes', models.CharField(blank=True, max_length=100)),
                ('planejamento', models.CharField(blank=True, max_length=100)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='ExameRetorno')),
                ('data_cadastro', models.DateField(auto_now_add=True, null=True)),
                ('valido', models.BooleanField(default=False)),
                ('data_validacao', models.DateTimeField(blank=True, null=True)),
                ('crianca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crianca.Crianca')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retorno_added_by', to=settings.AUTH_USER_MODEL)),
                ('validado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retorno_validated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='anamnese',
            name='image',
        ),
        migrations.AddField(
            model_name='anamnese',
            name='crianca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crianca.Crianca'),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='data_validacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='Anamnese'),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='validado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anamnese_validated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='valido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='anamnese',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anamnese_added_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
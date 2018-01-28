from .models import Anamnese, Retorno
from .models import ExameClinicoComDentes, ExameClinicoSemDentes
from .models import PrimeiraConsultaComDentes, PrimeiraConsultaSemDentes

import django_filters


class AnamneseFilter(django_filters.FilterSet):
    class Meta:
        model = Anamnese
        fields = ['data_cadastro', 'user']


class ExameClinicoComDentesFilter(django_filters.FilterSet):
    class Meta:
        model = ExameClinicoComDentes
        fields = ['data_cadastro', 'user']


class ExameClinicoSemDentesFilter(django_filters.FilterSet):
    class Meta:
        model = ExameClinicoSemDentes
        fields = ['data_cadastro', 'user']


class PrimeiraConsultaComDentesFilter(django_filters.FilterSet):
    class Meta:
        model = PrimeiraConsultaComDentes
        fields = ['data_cadastro', 'user']


class PrimeiraConsultaSemDentesFilter(django_filters.FilterSet):
    class Meta:
        model = PrimeiraConsultaSemDentes
        fields = ['data_cadastro', 'user']


class RetornoFilter(django_filters.FilterSet):
    class Meta:
        model = Retorno
        fields = ['data_cadastro', 'user']

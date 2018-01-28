from .models import Aluno
import django_filters


class AlunoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'data_nascimento']

from .models import Crianca
import django_filters


class CriancaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    nome_mae = django_filters.CharFilter(lookup_expr='icontains')
    nome_pai = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Crianca
        fields = ['nome', 'nome_mae', 'nome_pai', 'data_nascimento', 'user']

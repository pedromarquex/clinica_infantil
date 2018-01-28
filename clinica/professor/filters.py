from .models import Professor
import django_filters


class ProfessorFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Professor
        fields = ['nome', 'data_nascimento']

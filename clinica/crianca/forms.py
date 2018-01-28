from django.forms import ModelForm
from .models import Crianca


class CriancaForm(ModelForm):
    class Meta:
        model = Crianca
        fields = '__all__'

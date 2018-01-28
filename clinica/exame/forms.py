from django.forms import ModelForm
from .models import Anamnese, ExameClinicoComDentes
from .models import ExameClinicoSemDentes, PrimeiraConsultaComDentes
from .models import PrimeiraConsultaSemDentes
from .models import Retorno


class AnamneseForm(ModelForm):
    class Meta:
        model = Anamnese
        fields = '__all__'


class ClinicoComDentesForm(ModelForm):
    class Meta:
        model = ExameClinicoComDentes
        fields = '__all__'


class ClinicoSemDentesForm(ModelForm):
    class Meta:
        model = ExameClinicoSemDentes
        fields = '__all__'


class PrimeiraConsultaComDentesForm(ModelForm):
    class Meta:
        model = PrimeiraConsultaComDentes
        fields = '__all__'


class PrimeiraConsultaSemDentesForm(ModelForm):
    class Meta:
        model = PrimeiraConsultaSemDentes
        fields = '__all__'


class RetornoForm(ModelForm):
    class Meta:
        model = Retorno
        fields = '__all__'

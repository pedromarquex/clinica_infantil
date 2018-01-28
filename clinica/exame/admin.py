from django.contrib import admin
from .models import Anamnese, PrimeiraConsultaComDentes
from .models import PrimeiraConsultaSemDentes
from .models import ExameClinicoSemDentes
from .models import ExameClinicoComDentes
from .models import Retorno

admin.site.register(Anamnese)
admin.site.register(PrimeiraConsultaComDentes)
admin.site.register(PrimeiraConsultaSemDentes)
admin.site.register(ExameClinicoSemDentes)
admin.site.register(ExameClinicoComDentes)
admin.site.register(Retorno)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('aluno/', include('aluno.urls')),
    path('professor/', include('professor.urls')),
    path('crianca/', include('crianca.urls')),
    path('exame/', include('exame.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

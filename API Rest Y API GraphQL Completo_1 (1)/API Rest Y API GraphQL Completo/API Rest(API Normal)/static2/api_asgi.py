import os
import sys
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuración Django mínima
settings.configure(
    DEBUG=True,
    SECRET_KEY='clave-secreta',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
    ],
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'rest_framework',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR],  # buscar templates en el mismo directorio
        },
    ],
    STATIC_URL='/static/',
    DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
)

import django
django.setup()

from django.db import models
from rest_framework import serializers, viewsets, routers
from django.urls import path
from django.views.generic import TemplateView

# Modelo
class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    class Meta:
        app_label = 'miapp'

# Serializador
class MiModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiModelo
        fields = '__all__'

# ViewSet
class MiModeloViewSet(viewsets.ModelViewSet):
    queryset = MiModelo.objects.all()
    serializer_class = MiModeloSerializer

# Router
router = routers.DefaultRouter()
router.register(r'mimodelo', MiModeloViewSet)

# URLs
urlpatterns = [
    path('api/', lambda request: django.http.HttpResponse("API root. Use /api/mimodelo/")),
    path('api/mimodelo/', MiModeloViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('', TemplateView.as_view(template_name='index.html')),
]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    # Aplica migraciones automáticamente si no las hay
    execute_from_command_line([sys.argv[0], 'makemigrations', '--noinput'])
    execute_from_command_line([sys.argv[0], 'migrate', '--noinput'])

    # Ejecuta servidor en 127.0.0.1:8000 si no pasas args
    if len(sys.argv) == 1:
        sys.argv.append('runserver')
        sys.argv.append('127.0.0.1:8000')
    execute_from_command_line(sys.argv)

"""
URL configuration for pontos_turisticos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import PontoTuristicoSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoSet, basename='PontoTuristico')
router.register(r'avaliacoes', AvaliacaoViewSet, basename='Avaliacao')
router.register(r'endereco', EnderecoViewSet, basename='Endereco')
router.register(r'atracoes', AtracaoViewSet, basename='Atracao')
router.register(r'comentarios', ComentarioViewSet, basename='Comentario')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

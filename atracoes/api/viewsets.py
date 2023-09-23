from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import AtracoesSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    serializer_class = AtracoesSerializer
    filter_backends = {DjangoFilterBackend}
    filterset_fields = ['nome', 'descricao']

    def get_queryset(self):
        return Atracao.objects.all()

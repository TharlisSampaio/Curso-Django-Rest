from rest_framework.viewsets import ModelViewSet
from .serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        return Avaliacao.objects.all()

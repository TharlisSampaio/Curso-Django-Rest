from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecoViewSet(ModelViewSet):
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        return Endereco.objects.all()

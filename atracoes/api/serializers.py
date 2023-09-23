from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'horario_funcionamento', 'idade_minima', 'foto')

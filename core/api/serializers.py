from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'endereco', 'descricao_completa')

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

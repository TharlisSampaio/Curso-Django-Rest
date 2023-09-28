from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, DocIndentificacao
from atracoes.models import Atracao
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIndentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    # "This list may not be empty." que dizer que o campo é obrigatorio
    atracoes = AtracoesSerializer(many=True)  # read_only=True tira a obrigaroriadade
    endereco = EnderecoSerializer()  # campo relacionado
    doc_identificacao = DocIdentificacaoSerializer()
    # comentarios = ComentarioSerializer()
    # descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'endereco', 'avaliacoes', 'doc_identificacao')
        read_only_fields = ('comentarios', 'avaliacoes')  # campos como somente leitura

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']  # acessa a lista de atrações através da chave 'atracoes'
        del validated_data['atracoes']  # del palavra-chave é usada para excluir objetos.

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        doc = DocIndentificacao.objects.create(**doc)

        ponto.endereco = end
        ponto.doc_identificacao = doc

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

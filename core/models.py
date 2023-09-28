from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class DocIndentificacao(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    doc_identificacao = models.OneToOneField(DocIndentificacao, on_delete=models.CASCADE, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', blank=True, null=True)

    def __str__(self):
        return self.nome

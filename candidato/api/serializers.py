from rest_framework.serializers import ModelSerializer, StringRelatedField

from candidato.models import Candidato
from endereco.models import Endereco


class EnderecoCandidatoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'cep',
            'cidade',
            'estado',
        ]


class CandidatoSerializer(ModelSerializer):
    endereco = EnderecoCandidatoSerializer()

    class Meta:
        model = Candidato
        fields = [
            'id',
            'nome',
            'endereco'
        ]

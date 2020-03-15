from rest_framework.serializers import ModelSerializer, SerializerMethodField

from candidato.models import Candidato
from endereco.models import Endereco


class EnderecoCandidatoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class CandidatoSerializer(ModelSerializer):
    endereco = SerializerMethodField()

    class Meta:
        model = Candidato
        fields = [
            'id',
            'nome',
            'endereco'
        ]

    def endereco(self, obj):
        endereco = Endereco.objects.all().filter(cliente=obj.id)
        serializer = EnderecoCandidatoSerializer(endereco, many=False)
        return serializer.data

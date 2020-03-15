from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField, StringRelatedField

from candidato.models import Candidato
from voto.models import Voto


class VotoSerializer(ModelSerializer):
    def to_representation(self, instance):
        return {'candidato': Candidato.objects.get(pk=instance['candidato']).nome, 'votos': instance['votos']}

    class Meta:
        model = Voto
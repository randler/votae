from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField, StringRelatedField
from validate_docbr import CPF
from candidato.models import Candidato
from voto.models import Voto


class VotoSerializer(ModelSerializer):
    def to_representation(self, instance):
        return {'candidato': Candidato.objects.get(pk=instance['candidato']).nome, 'votos': instance['votos']}

    class Meta:
        model = Voto
        fields = '__all__'

    def validate(self, data):
        cpf = CPF()
        if not cpf.validate(data['cpf']):
            raise ValidationError({"cpf": "CPF Inválido!"})
        return data

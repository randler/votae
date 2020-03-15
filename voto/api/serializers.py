from rest_framework.serializers import ModelSerializer, SerializerMethodField

from voto.models import Voto


class VotoSerializer(ModelSerializer):
    class Meta:
        model = Voto
        fields = ['candidato']

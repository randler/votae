from rest_framework import generics

from candidato.models import Candidato
from .serializers import CandidatoSerializer


class CandidatoList(generics.ListAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

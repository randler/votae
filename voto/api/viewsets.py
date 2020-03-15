from rest_framework import generics

from voto.models import Voto
from .serializers import VotoSerializer


class VotoViewSet(generics.ListAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

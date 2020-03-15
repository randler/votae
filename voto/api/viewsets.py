from rest_framework import generics
from django.db.models import Count
from rest_framework.response import Response


from voto.models import Voto
from .serializers import VotoSerializer


class VotoViewSet(generics.ListAPIView):
    queryset = Voto

    def list(self, request):
        votos = Voto.objects.values('candidato').annotate(votos=Count('candidato')).order_by()
        serializer = VotoSerializer(votos, many=True)
        return Response(serializer.data)

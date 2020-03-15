from rest_framework import generics
from django.db.models import Count
from rest_framework.response import Response


from voto.models import Voto
from .serializers import VotoSerializer


class VotoViewSet(generics.ListAPIView):
    queryset = Voto

    def list(self, request, ):
        votos = Voto.objects.values('candidato').annotate(votos=Count('candidato')).order_by()
        total_votos = Voto.objects.all().count()
        serializer = VotoSerializer(votos, many=True)
        new_serializer = {
            'total_votos': total_votos,
            'resultado': list(serializer.data)
        }
        return Response(new_serializer)

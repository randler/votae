from rest_framework import generics, status
from django.db.models import Count
from rest_framework.response import Response


from voto.models import Voto
from .serializers import VotoSerializer


class VotoViewSet(generics.ListCreateAPIView):
    serializer_class = VotoSerializer
    queryset = Voto

    def list(self, request):
        votos = Voto.objects.values('candidato').annotate(votos=Count('candidato')).order_by()
        total_votos = Voto.objects.all().count()
        serializer = VotoSerializer(votos, many=True)
        new_serializer = {
            'total_votos': total_votos,
            'resultado': list(serializer.data)
        }
        return Response(new_serializer)

    def create(self, request, *args, **kwargs):
        data = request.data
        if data['recaptcha']:
            serializer = VotoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"save": True, "message": "Seu voto foi registrado Obrigado!"}, status=status.HTTP_201_CREATED)
            return Response({"save": False, "message": serializer.errors}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

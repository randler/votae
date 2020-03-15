from django.urls import path

from candidato.api.viewsets import CandidatoList

urlpatterns = [
    path('', CandidatoList.as_view()),
]

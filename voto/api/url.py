from django.urls import path

from voto.api.viewsets import VotoViewSet

urlpatterns = [
    path('', VotoViewSet.as_view()),
]

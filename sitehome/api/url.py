from django.urls import path

from sitehome.api.viewsets import Home

urlpatterns = [
    path('', Home.as_view()),
]

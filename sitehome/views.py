
from django.views.generic.base import View
from rest_framework.response import Response

import json

# Create your views here.


class HomePageView(View):
    def get(self):
        return Response({"api": "OK"})

from rest_framework.views import APIView
from rest_framework.response import Response

class ProductTempView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({"temp": 1})
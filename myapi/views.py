from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyDataSerializer

class MyDataView(APIView):
    def get(self, request):
        data = {'message': 'Hello, world!'}
        serializer = MyDataSerializer(data)
        return Response(serializer.data)

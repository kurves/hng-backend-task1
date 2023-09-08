from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Endpoint
from .serializers import EndpointSerializer



# Create your views here.
class EndPointAPIView(APIView):
    def get(self,request, *args, **kwargs):
        serializer= EndpointSerializer()
        return Response(serializer.data , status =status.HTTP_200_OK)


"""def index(request):
    return render(request, 'django_endpoint/index.html')"""
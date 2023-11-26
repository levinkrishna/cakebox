from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import UserSerializer,CakeSerializer
from cakebox.models import Cakes
# Create your views here.

class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



class CakesView(ModelViewSet):
    serializer_class=CakeSerializer
    model=Cakes
    queryset=Cakes.objects.all()
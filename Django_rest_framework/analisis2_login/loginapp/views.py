from django.shortcuts import render
from .models import UserUmg, Dormitorio, Programa
from .serializers import UserUmgSerializer, DormitorioSerializer, ProgramaSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class UserUmgViewSet(viewsets.ModelViewSet):
    # lookup_field = 'id'
    queryset = UserUmg.objects.all()
    serializer_class = UserUmgSerializer

class DormitorioViewSet(viewsets.ModelViewSet):
    # lookup_field = 'id'
    queryset = Dormitorio.objects.all()
    serializer_class = DormitorioSerializer

class ProgramaViewSet(viewsets.ModelViewSet):
    # lookup_field = 'id'
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

class UserLoginViewSet(viewsets.ModelViewSet):
    # lookup_field = 'id'
    queryset = UserUmg.objects.all()
    serializer_class = UserUmgSerializer

    def create(self, request):
        try:
            user = UserUmg.objects.get(username=request.data['username'])
            if user.password != request.data['password']:
                return Response("Invalid password", status=status.HTTP_409_CONFLICT)
            return Response("login ok", status=status.HTTP_200_OK)
        except:
            return Response("Invalid credentials", status=status.HTTP_409_CONFLICT)
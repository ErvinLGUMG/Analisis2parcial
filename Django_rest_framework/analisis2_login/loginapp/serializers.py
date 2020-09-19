from rest_framework import serializers
from .models import UserUmg, Dormitorio, Programa

class UserUmgSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = UserUmg
        fields = ('id','username','name')
        read_only_fields = ('id',)

class DormitorioSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Dormitorio
        fields = ('__all__')
        read_only_fields = ('id',)

class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Programa
        fields = ('__all__')
        read_only_fields = ('id',)
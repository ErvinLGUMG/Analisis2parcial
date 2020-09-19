from django.db import models

# Create your models here.
class UserUmg(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

class Dormitorio(models.Model):
    id = models.IntegerField(primary_key=True)
    numero = models.IntegerField(null=True, unique=True)
    habitacion = models.IntegerField(null=True)
    residente = models.IntegerField(null=True, unique=True)

class Programa(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    consejero = models.IntegerField(null=True, unique=True)



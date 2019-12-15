from django.shortcuts import render
from rest_framework import viewsets
from .models import Computador, PlacaMae, Processador
from .serializers import MontagemSerializer, PlacaMaeSerializer, ProcessadorSerializer

class MontagemView(viewsets.ModelViewSet):
    queryset = Computador.objects.all()
    serializer_class = MontagemSerializer

class PlacaMaeView(viewsets.ModelViewSet):
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer

class ProcessadorView(viewsets.ModelViewSet):
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer
    

from django.shortcuts import render
from judicial.models import Process, PartiesInvolved, PartiesInvolvedProcess
from rest_framework import viewsets
from judicial.serializers import ProcessSerializer, PartiesInvolvedSerializer, PartiesInvolvedProcessSerializer


def index(request):
    return render(request, 'index.html')

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

class PartiesInvolvedViewSet(viewsets.ModelViewSet):
    queryset = PartiesInvolved.objects.all()
    serializer_class = PartiesInvolvedSerializer

class PartiesInvolvedProcessViewSet(viewsets.ModelViewSet):
    queryset = PartiesInvolvedProcess.objects.all()
    serializer_class = PartiesInvolvedProcessSerializer


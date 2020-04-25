from django.shortcuts import render
from rest_framework import viewsets
from .models import Challenge, ChallengeData
from .serializers import ChallengeSerializer, ChallengeDataSerializer

class ChallengeView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class ChallengeDataView(viewsets.ModelViewSet):
    queryset = ChallengeData.objects.all()
    serializer_class = ChallengeDataSerializer
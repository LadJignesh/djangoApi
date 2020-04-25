from rest_framework import serializers
from .models import Challenge, ChallengeData

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'name', 'about')

class ChallengeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeData
        fields = ('id', 'name', 'instruction', 'mix', 'match')

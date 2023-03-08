from rest_framework import serializers
from .models import ChallengeAPI


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeAPI
        fields = '__all__'

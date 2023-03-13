# Importing the necessary classes from the rest_framework package
from rest_framework import serializers
# Importing the ChallengeAPI model from the models module within the same directory
from .models import ChallengeAPI


# Defining a serializer class for the ChallengeAPI model
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        # Specifying the model to be used
        model = ChallengeAPI
        # Specifying that all fields of the model should be included in the serialization
        fields = '__all__'

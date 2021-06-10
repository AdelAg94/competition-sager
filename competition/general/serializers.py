from rest_framework import serializers
from .models import Participant
from django.contrib.auth.models import User

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
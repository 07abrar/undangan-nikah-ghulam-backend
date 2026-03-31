from rest_framework import serializers
from .models import Couple, Event

class CoupleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Couple
        fields = ['id', 'groom_name', 'bride_name']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'date']
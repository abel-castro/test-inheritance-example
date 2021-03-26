from rest_framework import serializers
from .models import BasketballPlayer, SoccerPlayer


class BasketballPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BasketballPlayer


class SoccerPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SoccerPlayer

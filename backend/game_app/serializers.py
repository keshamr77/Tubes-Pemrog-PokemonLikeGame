from rest_framework import serializers
from .models import Leaderboard, PowerUp

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'

class PowerUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerUp
        fields = '__all__'

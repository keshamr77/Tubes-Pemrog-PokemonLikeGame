from rest_framework import viewsets
from .models import Leaderboard, PowerUp
from .serializers import LeaderboardSerializer, PowerUpSerializer
from django.shortcuts import render

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class PowerUpViewSet(viewsets.ModelViewSet):
    queryset = PowerUp.objects.all()
    serializer_class = PowerUpSerializer

def leaderboard_page(request):
    return render(request, 'leaderboard.html')
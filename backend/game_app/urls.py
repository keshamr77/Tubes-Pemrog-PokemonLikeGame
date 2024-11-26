from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'leaderboard', views.LeaderboardViewSet)  # Mengatur URL leaderboard
router.register(r'powerups', views.PowerUpViewSet)  # Mengatur URL powerups

urlpatterns = [
    path('leaderboard-page/', views.leaderboard_page, name='leaderboard_page'),
    path('leaderboard/', views.LeaderboardViewSet.as_view({'get': 'list'}), name='leaderboard'),
]

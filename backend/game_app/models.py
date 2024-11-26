from django.db import models

class Leaderboard(models.Model):
    username = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.username} - {self.score}"

class PowerUp(models.Model):
    powerup_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.powerup_name

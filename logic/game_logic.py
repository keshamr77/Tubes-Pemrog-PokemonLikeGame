class GameLogic:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.speed_multiplier = 1
        self.double_projectile = False

    def update_score(self, points):
        self.score += points

    def lose_life(self):
        self.lives -= 1
        return self.lives > 0  # Return True if game continues, False if over

    def reset_powerups(self):
        self.speed_multiplier = 1
        self.double_projectile = False

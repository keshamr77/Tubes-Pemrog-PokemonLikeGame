from django.test import TestCase
from game_app.models import Player
from game_app.services import update_score, check_collision

class PlayerModelTest(TestCase):

    def setUp(self):
        self.player = Player.objects.create(username="TestPlayer", score=0)

    def test_update_score(self):
        """
        Menguji apakah skor pemain berhasil diperbarui.
        """
        new_score = update_score(self.player, 50)
        self.assertEqual(new_score, 50)

    def test_collision_detection(self):
        """
        Menguji deteksi tabrakan antara pemain dan proyektil.
        """
        player_position = (10, 10)
        projectile_position = (13, 12)
        collision = check_collision(player_position, projectile_position)
        self.assertTrue(collision)

    def test_apply_powerup(self):
        """
        Menguji apakah power-up diterapkan ke pemain.
        """
        from game_app.services import apply_powerup
        apply_powerup(self.player, "invincibility")
        self.assertTrue(self.player.is_invincible)

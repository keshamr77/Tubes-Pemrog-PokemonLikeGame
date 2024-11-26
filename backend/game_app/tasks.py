from celery import shared_task
from game_app.models import Player, GameSession
import time

@shared_task
def reset_player_status(player_id):
    """
    Tugas background untuk mengembalikan status pemain ke keadaan normal setelah power-up habis.
    """
    time.sleep(10)  # Simulasi waktu habis (10 detik)
    try:
        player = Player.objects.get(id=player_id)
        player.is_invincible = False
        player.double_damage = False
        player.save()
    except Player.DoesNotExist:
        print("Player tidak ditemukan.")

@shared_task
def remove_expired_game_sessions():
    """
    Menghapus sesi game yang sudah kadaluwarsa untuk menjaga performa server.
    """
    expired_sessions = GameSession.objects.filter(is_active=False)
    expired_sessions.delete()

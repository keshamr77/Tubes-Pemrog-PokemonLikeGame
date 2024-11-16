from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import sys
from os.path import dirname, abspath

# Tambahkan path ke direktori utama proyek ke sys.path
base_path = dirname(dirname(abspath(__file__)))
sys.path.append(base_path)

# Inisialisasi Flask dan SocketIO
app = Flask(__name__)
socketio = SocketIO(app, async_mode='gevent')  # Ubah async_mode ke 'gevent' jika eventlet bermasalah

# Rute ke halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Fungsi untuk menjalankan game Pygame di thread terpisah
def start_pygame():
    from codes.main import Game  # Impor dilakukan di dalam fungsi
    game = Game()
    game.run()

# Jalankan server Flask dan Pygame
if __name__ == '__main__':
    # Jalankan thread Pygame hanya sekali di blok utama
    pygame_thread = threading.Thread(target=start_pygame)
    pygame_thread.start()

    # Jalankan Flask di localhost
    app.run(debug=True, port=5001)

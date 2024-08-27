from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from picamera import PiCamera
import time
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
camera = PiCamera()

def generate_frames():
    # Khởi động camera
    camera.start_preview()
    time.sleep(2)  # Đợi camera ổn định

    try:
        while True:
            # Chụp frame từ camera và lưu vào buffer
            frame_buffer = io.BytesIO()
            camera.capture(frame_buffer, format='jpeg')
            frame_buffer.seek(0)
            frame_bytes = frame_buffer.read()
            # Gửi frame đến client qua socketio
            socketio.emit('frame', {'image': frame_bytes}, namespace='/test')
            # Chờ 0.1 giây trước khi chụp frame tiếp theo
            time.sleep(0.1)
    finally:
        # Dừng camera khi kết thúc
        camera.stop_preview()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)

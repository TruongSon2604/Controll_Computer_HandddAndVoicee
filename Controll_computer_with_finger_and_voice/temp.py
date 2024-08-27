from flask import Flask, Response
from picamera import PiCamera
import time
import io

app = Flask(__name__)
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
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame_buffer.read() + b'\r\n')
            # Chờ 0.1 giây trước khi chụp frame tiếp theo
            time.sleep(0.1)
    finally:
        # Dừng camera khi kết thúc
        camera.stop_preview()

@app.route('/')
def index():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

# ১. প্রথমেই app ডিফাইন করতে হবে (এটি মিস হয়েছিল হয়তো)
app = Flask(__name__)

# ২. Mediapipe সেটআপ
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # ইমেজ প্রসেসিং
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_frame)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    # ফেস ডিটেকশন বক্স বা ল্যান্ডমার্ক দেখানোর কোড
                    cv2.putText(frame, "Pro AI: Tracking...", (10, 30), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # ফ্রেম এনকোডিং
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# ৩. এরপর রুটগুলো ডিফাইন করতে হবে
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# ৪. সবশেষে রান করানো
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
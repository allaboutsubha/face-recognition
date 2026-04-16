import cv2
import mediapipe as mp
# এরর হ্যান্ডেল করার জন্য সরাসরি ইমপোর্ট করার চেষ্টা
from mediapipe.python.solutions import face_mesh as mp_face_mesh

# তারপর কোডে ব্যবহার করুন:
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
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
            # ইমেজ প্রসেসিং (Anti-spoofing logic এখানে যোগ হবে)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_frame)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    # উদাহরণস্বরূপ একটি বক্স ড্র করা
                    h, w, c = frame.shape
                    cv2.rectangle(frame, (50, 50), (w-50, h-50), (0, 255, 0), 2)
                    cv2.putText(frame, "Liveness: Active", (60, 40), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # ফ্রেমকে ব্রাউজারে পাঠানোর জন্য এনকোড করা
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
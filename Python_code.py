from flask import Flask, render_template, Response
import cv2
import cmake
import dlib
import numpy as np
import time
import pygame

# Initialize Flask app
app = Flask(__name__)

# Initialize Pygame for sound
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound(r"C:\Users\Syed2\Desktop\Bootcamp2\Download Free Alarm Sound Effects _ Mixkit.html")  # Path to alarm sound

# Load pre-trained models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Constants
EYE_CLOSED_THRESHOLD = 0.25  # Threshold for eye aspect ratio
CONSECUTIVE_FRAMES = 30  # Number of frames to consider for drowsiness (3 seconds at 10 FPS)

# Function to calculate eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Function to generate video frames
def generate_frames():
    cap = cv2.VideoCapture(0)  # Access webcam
    counter = 0
    alarm_on = False

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            for face in faces:
                landmarks = predictor(gray, face)
                landmarks = np.array([(p.x, p.y) for p in landmarks.parts()])

                # Extract left and right eye landmarks
                left_eye = landmarks[42:48]
                right_eye = landmarks[36:42]

                # Calculate EAR for both eyes
                left_ear = eye_aspect_ratio(left_eye)
                right_ear = eye_aspect_ratio(right_eye)
                ear = (left_ear + right_ear) / 2.0

                # Check if eyes are closed
                if ear < EYE_CLOSED_THRESHOLD:
                    counter += 1
                    if counter >= CONSECUTIVE_FRAMES:
                        if not alarm_on:
                            alarm_sound.play()
                            alarm_on = True
                        cv2.putText(frame, "DROWSINESS DETECTED!", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    counter = 0
                    alarm_on = False

                # Draw eye landmarks
                for (x, y) in left_eye:
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                for (x, y) in right_eye:
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route for the video feed
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
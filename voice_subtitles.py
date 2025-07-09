import cv2
import speech_recognition as sr
from collections import deque
import textwrap
import time

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize speech recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Configure recognizer
recognizer.pause_threshold = 0.6
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

# Subtitles & status
subtitle_text = ""
history = deque(maxlen=5)
status = "listening"
last_speech_time = time.time()

# Callback for background recognition
def callback(recognizer, audio):
    global subtitle_text, history, status, last_speech_time
    try:
        text = recognizer.recognize_google(audio)
        if text.strip():
            subtitle_text = text
            history.appendleft(text)
            status = "listening"
            last_speech_time = time.time()
            print(f">> You said: {text}")
    except sr.UnknownValueError:
        if time.time() - last_speech_time < 3:
            subtitle_text = "(Could not understand)"
            status = "error"
            print(">> Could not understand.")
    except sr.RequestError:
        subtitle_text = "(No Internet)"
        status = "no_internet"
        print(">> No internet connection.")

# Start background listening
stop_listening = recognizer.listen_in_background(mic, callback, phrase_time_limit=4)

# Font and colors
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (0, 255, 255)
dot_color = {
    "listening": (0, 255, 0),
    "error": (0, 0, 255),
    "no_internet": (0, 0, 255)
}
max_line_chars = 45

# ---- MAIN LOOP ----
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Listening dot
    cv2.circle(gray, (30, 30), 10, dot_color.get(status, (0, 255, 0)), -1)

    # Subtitle history
    draw_y = 400
    line_height = 28
    for line in list(history):
        for l in reversed(textwrap.wrap(line, width=max_line_chars)):
            if draw_y < 50:
                break
            cv2.putText(gray, l, (20, draw_y), font, 0.6, text_color, 2, cv2.LINE_AA)
            draw_y -= line_height

    # Current subtitle (bottom)
    wrapped = textwrap.wrap(subtitle_text, width=max_line_chars)
    for i, line in enumerate(wrapped[-3:]):
        y = 470 + i * 30
        cv2.putText(gray, line, (20, y), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Real-Time Subtitles", gray)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
stop_listening()

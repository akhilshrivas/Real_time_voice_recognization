# 🎙️ Real-Time Voice Subtitles with Python 🖥️

This project provides **real-time speech-to-text subtitles** using your **microphone and webcam**. It captures voice input, transcribes it using Speech Recognition, and overlays the spoken text as subtitles on your webcam video feed using OpenCV.

---

## 📌 Features

- 🧠 Real-time **speech recognition**
- 🎥 Live **webcam feed** with subtitles
- 📝 Displays **latest spoken sentences** with history
- 🟢 Visual **status indicator** for:
  - Listening
  - Errors
  - No internet
- 🔁 Auto-updating subtitles using background processing

---

## 🛠️ Tech Stack

- Python
- OpenCV (`cv2`)
- SpeechRecognition (`speech_recognition`)
- PyAudio (for microphone access)
- Deque & Textwrap (for subtitle formatting)

---

## ▶️ Getting Started

### 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/akhilshrivas/Real_time_voice_recognization.git
   cd Real_time_voice_recognization
Install dependencies:

bash
Copy code
pip install opencv-python speechrecognition pyaudio
If PyAudio gives an error, install it using:

nginx
Copy code
pip install pipwin
pipwin install pyaudio
🚀 Run the Project
bash
Copy code
python your_script_name.py
Press ESC to exit the video window.

Copy code
Real_time_voice_recognization/
├── main.py
├── README.md
└── ...
📌 To Do / Future Improvements
Add hand gesture controls (e.g., to highlight or correct subtitles)

Add voice-to-text saving to file

Integrate with ChatGPT to respond to spoken questions

Improve error handling and UI

👨‍💻 Author
Akhil Shrivas

GitHub: @akhilshrivas
Gmail: akhilshrivas0@gmail.com

📜 License
This project is open-source and available under the MIT License.

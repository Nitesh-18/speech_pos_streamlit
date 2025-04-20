# 🎵 Speech-to-Text with POS Tagging Web App

A real-time AI-powered web application that converts **speech to text** using OpenAI's Whisper model and performs **Part-of-Speech (POS) tagging** using spaCy. Built with Streamlit for an interactive and responsive UI.

---

## 🚀 Features

- 🎤 **Live microphone input or audio file upload**
- 🌤️ **Automatic transcription** using Whisper
- 🧐 **POS tagging** with spaCy NLP
- 📊 Interactive **table display** of text with corresponding POS tags
- 🌐 Simple, clean, browser-based UI with **Streamlit**

---

## 📸 Demo

> Coming Soon! (Add screenshots or a short GIF of the app in action)

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/speech-pos-streamlit.git
cd speech-pos-streamlit
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> Make sure you have **FFmpeg** installed and added to your PATH.  
[Download FFmpeg](https://www.gyan.dev/ffmpeg/builds/)

### 4. Download Whisper Model (Optional)
Whisper will automatically download the required model (like `base` or `small`) on first use.

---

## ▶️ Usage

### Run the app:
```bash
streamlit run app.py
```

### Use the App:
- Speak into your mic (or upload an audio file)
- The app will:
  - Transcribe your voice to text (via Whisper)
  - Analyze and tag parts of speech (via spaCy)
  - Display a table of words and their POS tags

---

## 🧹 Tech Stack

| Tool        | Purpose                     |
|-------------|-----------------------------|
| [Whisper](https://github.com/openai/whisper) | Speech-to-text (ASR)         |
| [spaCy](https://spacy.io/)                | POS tagging (NLP)            |
| [Streamlit](https://streamlit.io/)        | Web UI / Frontend            |
| [PyDub](https://github.com/jiaaro/pydub)  | Audio processing             |
| FFmpeg                                     | Audio format conversion      |

---

## 📂 Project Structure

```
speech_pos_streamlit/
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── utils/
│   └── helpers.py         # (optional) Helper functions
└── assets/                # (optional) Images, audio, etc.
```

---

## ⚠️ Troubleshooting

- ❌ **FFmpeg not found error?**
  - Make sure `ffmpeg.exe` is added to your system PATH.
  - Test with: `ffmpeg -version` in CMD/Terminal.

- ⚠️ **Some frames dropped?**
  - This warning is from audio queueing in real-time mic mode. You can try switching to audio file mode for stable results.

- 💡 **FP16 not supported?**
  - On CPU, Whisper defaults to FP32 — this is normal and safe to ignore.

---

## 📌 Future Improvements

- 🌍 Multilingual transcription
- 🎈 Sentiment analysis
- 💬 Entity Recognition
- 📝 Export to PDF/CSV

---

## 🙌 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)
- [spaCy NLP](https://spacy.io/)
- [Streamlit](https://streamlit.io/)
- [Gyan.dev FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/)

---

## ⭐️ Show Some Love

If you liked this project, please consider giving it a ⭐ on [GitHub](https://github.com)!

---


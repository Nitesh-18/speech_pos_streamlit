import streamlit as st
import os
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, ClientSettings

# Replace with your actual ffmpeg.exe path
# ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
ffmpeg_path = "ffmpeg"  # Assume ffmpeg is in PATH
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)
import whisper
import spacy
import numpy as np
import av
import tempfile
import pandas as pd
from pydub.utils import which
from pydub import AudioSegment

AudioSegment.converter = which("ffmpeg")

# Load models once
whisper_model = whisper.load_model("base")
nlp = spacy.load("en_core_web_sm")

st.title("🎤 Real-Time Speech-to-Text + POS Tagging")
st.markdown("Record from mic or upload audio to transcribe and tag parts of speech.")

# --- Audio Upload Section ---
uploaded_audio = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])


def transcribe_and_tag(audio_path):
    # Transcribe with Whisper
    result = whisper_model.transcribe(audio_path)
    transcription = result["text"]

    # POS tagging
    doc = nlp(transcription)
    pos_data = [(token.text, token.pos_, token.tag_) for token in doc]

    return transcription, pos_data


# If file is uploaded
if uploaded_audio is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_audio.read())
        audio_path = tmp.name

    # Convert to wav if needed
    sound = AudioSegment.from_file(audio_path)
    wav_path = audio_path.replace(".mp3", ".wav")
    sound.export(wav_path, format="wav")

    st.info("Transcribing uploaded audio...")
    transcription, pos_data = transcribe_and_tag(wav_path)

    st.subheader("📝 Transcription")
    st.write(transcription)

    st.subheader("📊 POS Tags")
    df = pd.DataFrame(pos_data, columns=["Token", "POS", "Detailed Tag"])
    st.dataframe(df)

    os.remove(audio_path)
    os.remove(wav_path)

# --- Real-time Mic Input Section ---

st.markdown("### 🎙️ Or Record Live Audio from Microphone")


class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.recorded_frames = []

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray()
        self.recorded_frames.append(audio)
        return frame

    def get_wav_bytes(self):
        if self.recorded_frames:
            audio_np = np.concatenate(self.recorded_frames)
            audio_segment = AudioSegment(
                audio_np.tobytes(), frame_rate=48000, sample_width=2, channels=1
            )
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
                audio_segment.export(tmp_wav.name, format="wav")
                return tmp_wav.name
        return None


ctx = webrtc_streamer(
    key="mic",
    audio_processor_factory=AudioProcessor,
    client_settings=ClientSettings(
        media_stream_constraints={"audio": True, "video": False},
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    ),
)

if ctx.audio_processor:
    if st.button("Transcribe Mic Input"):
        with st.spinner("Processing..."):
            audio_path = ctx.audio_processor.get_wav_bytes()
            if audio_path:
                transcription, pos_data = transcribe_and_tag(audio_path)
                st.subheader("📝 Transcription")
                st.write(transcription)
                st.subheader("📊 POS Tags")
                df = pd.DataFrame(pos_data, columns=["Token", "POS", "Detailed Tag"])
                st.dataframe(df)
                os.remove(audio_path)
            else:
                st.warning("No audio recorded.")

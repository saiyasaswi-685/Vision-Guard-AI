from gtts import gTTS
from pathlib import Path

audio_dir = Path("alerts/audio")
audio_dir.mkdir(parents=True, exist_ok=True)

# English
english = gTTS(text="Please wear a helmet", lang="en")
english.save(audio_dir / "english.mp3")

# Telugu
telugu = gTTS(text="దయచేసి హెల్మెట్ ధరించండి", lang="te")
telugu.save(audio_dir / "telugu.mp3")

# Hindi
hindi = gTTS(text="कृपया हेलमेट पहनें", lang="hi")
hindi.save(audio_dir / "hindi.mp3")

print("Audio files created successfully!")
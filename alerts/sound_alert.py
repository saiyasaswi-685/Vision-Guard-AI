from pathlib import Path
import threading
import pygame
import time


class SoundAlert:
    def __init__(self) -> None:
        pygame.mixer.init()

        self.audio_files = [
            Path("alerts/audio/english.mp3"),
            Path("alerts/audio/telugu.mp3"),
            Path("alerts/audio/hindi.mp3"),
        ]

        self.current_index = 0
        self.last_play_time = 0
        self.cooldown = 1

    def play(self) -> None:
        current_time = time.time()

        if current_time - self.last_play_time < self.cooldown:
            return

        self.last_play_time = current_time

        thread = threading.Thread(target=self._play_sound, daemon=True)
        thread.start()

    def _play_sound(self) -> None:
        try:
            audio_path = self.audio_files[self.current_index]

            if audio_path.exists():
                pygame.mixer.music.load(str(audio_path))
                pygame.mixer.music.play()

            self.current_index = (self.current_index + 1) % len(self.audio_files)

        except Exception as error:
            print(f"Unable to play sound alert: {error}")
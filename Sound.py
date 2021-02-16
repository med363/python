import io
import pygame
from gtts import gTTS
def speak(text):
    with io.BytesIO() as file :
        gTTS (text = text , lang="en") , write_to_fo(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.load(file).play()
        while pygame.mixer.music.get_busy():
            continue
if __name__ == '__main__':
    text = input ("what should : say? > ")
    speak(text)
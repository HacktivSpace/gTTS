import os
import pygame
from gtts import gTTS
from queue import Queue
import threading

pygame.mixer.init()

text_queue = Queue()

def add_text_to_queue(text):
    text_queue.put(text)

def tts_worker():
    while True:
        text = text_queue.get()
        tts = gTTS(text=text, lang='en')
        tts.save('temp_audio.mp3')
        pygame.mixer.music.load('temp_audio.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        text_queue.task_done()

thread = threading.Thread(target=tts_worker, daemon=True)
thread.start()

while True:
    text = input("Enter text to speak (or 'exit' to quit): ")
    if text.lower() == 'exit':
        break
    add_text_to_queue(text)

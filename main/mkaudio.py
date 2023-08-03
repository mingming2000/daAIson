from blindbee import TextToSpeech
import pygame

# t = TextToSpeech()
# t.testing('Please detect QR code.')
# t.testing('Please tell me the qr number.')
# t.testing('Please tell me the object name.')
# t.testing("Standby. Call if needed.")
# t.testing("What can I help you?")
# t.testing("Please say again.")

music_file = "/home/dspi/daAIson/main/audiofiles/What can I help you?.linear16"

pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play
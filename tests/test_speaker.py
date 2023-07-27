import pygame
import time

pygame.mixer.init()
p = pygame.mixer.Sound('/home/dspi/daAIson/tests/test_tts.linear16')    # audio file must be 16 bits.

while True:
    p.play()
    time.sleep(3.0)
    p.stop()
    break


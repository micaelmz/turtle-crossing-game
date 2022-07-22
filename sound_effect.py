import pygame

pygame.init()
sound = pygame.mixer.music


def background_sound(stop=False):
    sound.load('sounds/background_sound.mp3')
    sound.set_volume(0.2)
    sound.play(-1)
    if stop:
        sound.stop()


def game_over():
    sound.load('sounds/game_over.mp3')
    sound.play()

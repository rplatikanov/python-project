import pygame


class Graphics:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

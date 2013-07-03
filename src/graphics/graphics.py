import pygame
import os


class Graphics:
    RES_DIR = os.path.join('..', 'res')

    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Cave Challenge')

        self.ship_image = pygame.transform.scale(pygame.image.load(os.path.join(self.RES_DIR, 'ship.png')), (50, 50))
        self.terrain = pygame.image.load(os.path.join(self.RES_DIR, 'testmap.png'))


class ShipSprite(pygame.sprite.Sprite):
    pass


class RocketSprite(pygame.sprite.Sprite):
    pass

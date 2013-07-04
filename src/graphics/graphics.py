import pygame
import os
from util.vec2d import Vec2D
import math


class Graphics:
    RES_DIR = os.path.join('..', 'res')
    CAPTION = 'Cave Challenge'
    SHIP_IMAGE = 'ship.png'
    SHIP_WIDTH = 50

    class Layer:
        def __init__(self, image, tiled, speed, graphics, blend_mode):
            if tiled:
                self.num_tiles = max(2, math.ceil(graphics.screen.get_width() / image.get_width() + 1))
                self.image = pygame.surface.Surface((image.get_width() * self.num_tiles, image.get_height()))

                for i in range(self.num_tiles):
                    self.image.blit(image, (image.get_width() * i, 0))

            else:
                self.image = image

            self.tiled = tiled
            self.speed = speed
            self.graphics = graphics
            self.blend_mode = blend_mode

        def get_layer_pos(self):
            if self.tiled:
                image_width = self.image.get_width() // self.num_tiles

                posx = (self.graphics.camerapos.x * self.speed) % image_width

                if posx < 0:
                    posx += image_width

                elif (posx > image_width):
                    posx -= image_width

                return Vec2D(-posx, 0)

            else:
                return -self.graphics.camerapos * self.speed

    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(Graphics.CAPTION)
        self.load_images()

    def load_images(self):
        ship_tex = Graphics.load_image(Graphics.SHIP_IMAGE)
        scale = Graphics.SHIP_WIDTH / ship_tex.get_width()
        self.ship_image = pygame.transform.scale(ship_tex, Graphics.scale_size(ship_tex.get_size(), scale))
        self.terrain = Graphics.load_image('testmap.png')

        self.layers = []

        hazetex = Graphics.load_image('testhaze.png')
        haze = Graphics.Layer(hazetex, True, 1.5, self, pygame.BLEND_RGBA_ADD)
        self.layers.append(haze)
        self.layers.append(Graphics.Layer(self.terrain, False, 1, self, 0))

    @staticmethod
    def load_image(name):
        image = pygame.image.load(os.path.join(Graphics.RES_DIR, name)).convert_alpha()

        return image

    @staticmethod
    def scale_size(size, scale):
        new_width = int(size[0] * scale)
        new_height = int(size[1] * scale)

        return (new_width, new_height)


class ShipSprite(pygame.sprite.Sprite):
    pass


class RocketSprite(pygame.sprite.Sprite):
    pass

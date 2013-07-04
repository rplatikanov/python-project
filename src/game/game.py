from graphics.graphics import Graphics
import os
import pygame
from base.world import *
from base.movable import *


class Game:
    def __init__(self):
        self.graphics = Graphics(320, 480)
        self.world = World(640, 480, None)

        self.world.ship = Ship(pygame.Rect(100, 100, self.graphics.ship_image.get_width(), self.graphics.ship_image.get_height()))

        self.running = False

    def run(self):
        self.running = True
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(60)
            self.handle_events()
            self.world.iterate(dt)
            self.calculate_camera()

            self.graphics.screen.fill((10, 50, 200))
            self.graphics.screen.blit(self.graphics.ship_image, tuple(self.world.ship.pos - self.graphics.camerapos))

            for l in self.graphics.layers:
                self.graphics.screen.blit(l.image, tuple(l.get_layer_pos()), None, l.blend_mode)

            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.world.ship.vel += Vec2D(0, -0.2)
                    elif event.key == pygame.K_DOWN:
                        self.world.ship.vel += Vec2D(0, 0.2)
                    elif event.key == pygame.K_LEFT:
                        self.world.ship.vel += Vec2D(-0.2, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.world.ship.vel += Vec2D(0.2, 0)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.world.ship.vel -= Vec2D(0, -0.2)
                    elif event.key == pygame.K_DOWN:
                        self.world.ship.vel -= Vec2D(0, 0.2)
                    elif event.key == pygame.K_LEFT:
                        self.world.ship.vel -= Vec2D(-0.2, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.world.ship.vel -= Vec2D(0.2, 0)

    def calculate_camera(self):
        self.graphics.camerapos = Vec2D(self.world.ship.pos.x - 100, 0)

from graphics.graphics import Graphics, RocketSprite
import os
import pygame
from base.world import *
from base.movable import *


class Game:
    def __init__(self):
        height = 600
        self.graphics = Graphics(1200, height)
        self.world = World(self.graphics.terrain.get_width(), height, self.graphics.terrain)

        self.world.ship = Ship(Vec2D(100, 100), Vec2D(self.graphics.ship_image.get_width(), self.graphics.ship_image.get_height()))

        self.rockets = pygame.sprite.Group()

        self.running = False

    def run(self):
        self.running = True
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(60)
            self.handle_events()
            self.world.iterate(dt)
            self.calculate_camera()

            self.rockets.update()

            self.graphics.screen.fill((40, 40, 40))
            
            for l in self.graphics.layers:
                self.graphics.screen.blit(l.image, tuple(l.get_layer_pos()), None, l.blend_mode)
            
            self.graphics.screen.blit(self.graphics.ship_image, tuple(self.world.ship.pos - self.graphics.camerapos))
            self.rockets.draw(self.graphics.screen)

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
                    elif event.key == pygame.K_SPACE:
                        self.shoot()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.world.ship.vel -= Vec2D(0, -0.2)
                    elif event.key == pygame.K_DOWN:
                        self.world.ship.vel -= Vec2D(0, 0.2)
                    elif event.key == pygame.K_LEFT:
                        self.world.ship.vel -= Vec2D(-0.2, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.world.ship.vel -= Vec2D(0.2, 0)

        for event in list(self.world.events):
            self.world.events.remove(event)
            if isinstance(event, RocketHitGround):
                blast = pygame.surface.Surface((event.blast_radius * 2, event.blast_radius * 2), 0, self.graphics.terrain)
                pygame.draw.circle(blast, (255, 255, 255), (event.blast_radius, event.blast_radius), event.blast_radius)
                self.graphics.terrain.blit(blast, tuple(event.coords + -Vec2D(event.blast_radius, event.blast_radius)), None, pygame.BLEND_RGBA_SUB)

    def calculate_camera(self):
        self.graphics.camerapos = Vec2D(self.world.ship.pos.x - 100, 0)

    def shoot(self):
        rocket = self.world.shoot()
        sprite = RocketSprite(rocket, self.graphics, self.rockets)






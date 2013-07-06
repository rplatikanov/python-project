import unittest
from base.world import World
import os
import pygame
from base.movable import Ship, Rocket
from util.vec2d import Vec2D


class WorldTest(unittest.TestCase):
    RES_DIR = os.path.join('..', '..', 'res')

    def setUp(self):
        terrain = pygame.image.load(os.path.join(self.RES_DIR,
                                                       'testmap.png'))
        self.world = World(terrain.get_width(), terrain.get_height(),
                           terrain)
        self.world.ship = Ship(Vec2D(100, 100), Vec2D(50, 50))

    def test_shoot_rocket(self):
        self.assertIsNotNone(self.world.shoot())

    def test_ship_collision(self):
        self.world.check_ship_collisions()
        self.assertTrue(self.world.ship.alive)

        self.world.ship.pos = Vec2D(200, 50)
        self.world.check_ship_collisions()
        self.assertFalse(self.world.ship.alive)

        self.world.ship.pos = Vec2D(-10, -50)
        self.world.check_ship_collisions()

    def test_rocket_ship_collision(self):
        rocket = Rocket(Vec2D(200, 100), Vec2D(10, 10))
        self.world.check_rocket_movable_collisions(rocket)
        self.assertTrue(self.world.ship.alive)

        rocket.pos = Vec2D(100, 100)
        self.world.check_rocket_movable_collisions(rocket)
        self.assertFalse(self.world.ship.alive)

    def test_rocket_ground_collision(self):
        rocket = Rocket(Vec2D(100, 100), Vec2D(10, 10))
        self.world.check_rocket_ground_collisions(rocket)
        self.assertTrue(rocket.alive)
        self.assertEqual(0, len(self.world.events))

        rocket.pos = Vec2D(200, 50)
        self.world.check_rocket_ground_collisions(rocket)
        self.assertFalse(rocket.alive)
        self.assertEqual(1, len(self.world.events))

    def test_ship_shoot(self):
        self.assertIsNotNone(self.world.ship.shoot_rocket())

    def test_enemy_shoot(self):
        rocket = self.world.ship.shoot_rocket()
        self.assertIsNotNone(rocket)

if __name__ == "__main__":
    unittest.main()

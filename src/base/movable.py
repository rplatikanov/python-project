from util.vec2d import Vec2D
import pygame


class Movable:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.vel = Vec2D(0, 0)
        self.alive = True

    def get_rect(self):
        return pygame.Rect(tuple(self.pos), tuple(self.size))


class Ship(Movable):
    def __init__(self, pos, size):
        Movable.__init__(self, pos, size)
        self.power_up = False
        self.power_down = False
        self.power_forward = True

    def shoot_rocket(self):
        rocket = Rocket(Vec2D(self.pos.x + self.size.x, self.pos.y + self.size.y / 2), Vec2D(Rocket.SIZE[0], Rocket.SIZE[1]))
        rocket.vel = Vec2D(0.5, 0)
        return rocket

    def set_power_up(self, power):
        self.power_up = power

    def set_power_down(self, power):
        self.power_down = power

    def set_power_forward(self, power):
        self.power_forward = power


class Rocket(Movable):
    SIZE = (10, 5)

    def __init__(self, pos, size):
        Movable.__init__(self, pos, size)
        self.flight_time = 0

    def get_blast_radius(self):
        return 50

    def get_max_flight_time(self):
        return 3000


class Enemy(Movable):
    def __init__(self, pos, size):
        Movable.__init__(self, pos, size)
        self.timer = 0

    def is_in_range(self, target):
        distance = self.pos.x - target.pos.x
        return distance < 1000 and distance >= 0

    def shoot(self):
        rocket = Rocket(Vec2D(self.pos.x - Rocket.SIZE[0], self.pos.y + self.size.y / 2), Vec2D(Rocket.SIZE[0], Rocket.SIZE[1]))
        rocket.vel = Vec2D(-0.5, 0)
        return rocket

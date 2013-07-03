from collections import deque


class World:
    def __init__(self, width, height, collision_map):
        self.width = width
        self.height = height
        self.collision_map = collision_map
        self.ship = None
        self.rockets = set()
        self.enemies = set()
        self.events = deque()

    def iterate(self, dt):
        self.ship.pos += self.ship.vel * dt

    def check_ship_collisions(self):
        pass

    def check_rocket_collisions(self):
        pass

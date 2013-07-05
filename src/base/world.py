from collections import deque
from base.events import RocketHitGround


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
        if (self.ship.pos.x < 0):
            self.ship.pos.x = 0

        self.check_ship_collisions()

        destroyed = []
        for rocket in self.rockets:
            rocket.pos += rocket.vel * dt
            if self.check_rocket_collisions(rocket):
                destroyed.append(rocket)
                rocket.blown = True
                self.events.append(RocketHitGround(rocket.pos, rocket.get_blast_radius()))

        for rocket in destroyed:
            self.rockets.remove(rocket)

    def shoot(self):
        rocket = self.ship.shoot_rocket()
        self.rockets.add(rocket)
        return rocket

    def check_ship_collisions(self):
        for y in range(int(self.ship.pos.y), int(self.ship.pos.y + self.ship.size.y)):
            for x in range(int(self.ship.pos.x), int(self.ship.pos.x + self.ship.size.x)):
                c = self.collision_map.get_at((x, y))
                if c[3] != 0:
                    return True

        return False


    def check_rocket_collisions(self, rocket):
        if rocket.pos.x + rocket.size.x >= self.width:
            return True

        for y in range(int(rocket.pos.y), int(rocket.pos.y + rocket.size.y)):
            for x in range(int(rocket.pos.x), int(rocket.pos.x + rocket.size.x)):
                c = self.collision_map.get_at((x, y))
                if c[3] != 0:
                    return True

        return False

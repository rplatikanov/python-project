from collections import deque
from base.events import RocketHitGround, EnemyShoot, ShipDead


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
        if self.ship.alive:
            self.ship.pos += self.ship.vel * dt
            if (self.ship.pos.x < 0):
                self.ship.pos.x = 0

            if self.ship.power_up:
                self.ship.vel.y -= 0.0007 * dt * dt / 2
            if self.ship.power_down:
                self.ship.vel.y += 0.0007 * dt * dt / 2
            if self.ship.power_forward:
                self.ship.vel.x = 0.1

            self.ship.vel.y *= 0.85

            self.check_ship_collisions()

        for enemy in self.enemies:
            enemy.timer += dt
            if enemy.timer > 1000:
                enemy.timer = 0
                if enemy.is_in_range(self.ship):
                    rocket = enemy.shoot()
                    self.rockets.add(rocket)
                    self.events.append(EnemyShoot(rocket))

        destroyed = set()
        for rocket in self.rockets:
            rocket.pos += rocket.vel * dt
            rocket.flight_time += dt
            if rocket.flight_time > rocket.get_max_flight_time():
                rocket.alive = False

            self.check_rocket_ground_collisions(rocket)

            self.check_rocket_movable_collisions(rocket)

            if not rocket.alive:
                destroyed.add(rocket)

        for rocket in destroyed:
            self.rockets.remove(rocket)

    def add_enemy(self, enemy):
        self.enemies.add(enemy)

    def shoot(self):
        rocket = self.ship.shoot_rocket()
        self.rockets.add(rocket)
        return rocket

    def check_ship_collisions(self):
        collision = False
        if self.ship.pos.x < 0:
            collision = True
        elif self.ship.pos.x + self.ship.size.x >= self.width:
            collision = True
        if self.ship.pos.y < 0:
            collision = True
        elif self.ship.pos.y + self.ship.size.y >= self.height:
            collision = True

        if not collision:
            for y in range(int(self.ship.pos.y), int(self.ship.pos.y + self.ship.size.y)):
                for x in range(int(self.ship.pos.x), int(self.ship.pos.x + self.ship.size.x)):
                    c = self.collision_map.get_at((x, y))
                    if c[3] != 0:
                        collision = True

        if collision:
            self.ship.alive = False
            self.events.append(ShipDead())

    def check_rocket_ground_collisions(self, rocket):
        collision = False
        if rocket.pos.x + rocket.size.x >= self.width:
            collision = True
        elif rocket.pos.x < 0:
            collision = True

        if not collision:
            for y in range(int(rocket.pos.y), int(rocket.pos.y + rocket.size.y)):
                for x in range(int(rocket.pos.x), int(rocket.pos.x + rocket.size.x)):
                    c = self.collision_map.get_at((x, y))
                    if c[3] != 0:
                        collision = True

        if collision:
            rocket.alive = False
            self.events.append(RocketHitGround(rocket.pos, rocket.get_blast_radius()))

    def check_rocket_movable_collisions(self, rocket):
        for enemy in list(self.enemies):
            if enemy.get_rect().colliderect(rocket.get_rect()):
                self.enemies.remove(enemy)
                enemy.alive = False
                rocket.alive = False

        if self.ship.get_rect().colliderect(rocket.get_rect()):
            self.ship.alive = False
            rocket.alive = False
            self.events.append(ShipDead())


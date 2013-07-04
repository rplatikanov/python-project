from util.vec2d import Vec2D


class Movable:
    def __init__(self, pos, size):
        # self.pos = Vec2D(rect.left, rect.top)
        self.pos = pos
        self.size = size
        # self.rect = rect
        self.vel = Vec2D(0, 0)
        # self.acc = Vec2D(0, 0)


class Ship(Movable):
    def __init__(self, pos, size):
        Movable.__init__(self, pos, size)

    def shoot_rocket(self):
        rocket = Rocket(Vec2D(self.pos.x + self.size.x * 2 / 2, self.pos.y + self.size.y / 2), Vec2D(Rocket.SIZE[0], Rocket.SIZE[1]))
        rocket.vel = Vec2D(0.5, 0)
        return rocket


class Rocket(Movable):
    SIZE = (10, 5)

    def __init__(self, pos, size):
        Movable.__init__(self, pos, size)
        self.flight_time = 0

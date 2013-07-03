from util.vec2d import Vec2D


class Movable:
    def __init__(self, rect):
        self.pos = Vec2D(rect.left, rect.top)
        self.rect = rect
        self.vel = Vec2D(0, 0)
        self.acc = Vec2D(0, 0)


class Ship(Movable):
    def __init__(self, rect):
        Movable.__init__(self, rect)


class Rocket(Movable):
    def __init__(self, rect):
        Movable.__init__(self, rect)

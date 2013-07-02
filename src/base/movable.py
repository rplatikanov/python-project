from util.vec2d import Vec2D


class Movable:
    def __init__(self, rect):
        self.rect = rect
        self.vel = Vec2D(0, 0)
        self.acc = Vec2D(0, 0)


class Character(Movable):
    def __init__(self, rect):
        Movable.__init__(self, rect)


class Rocket(Movable):
    def __init__(self, rect):
        Movable.__init__(self, rect)

from collections import deque


class World:
    def __init__(self, width, height, collisionMap):
        self.width = width
        self.height = height
        self.collisionMap = collisionMap
        self.character = None
        self.rockets = set()
        self.enemies = set()
        self.events = deque()

    def iterate(self, dt):
        pass

    def checkCharacterCollisions(self):
        pass

    def checkRocketCollisions(self):
        pass

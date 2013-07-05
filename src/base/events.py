class ShipHitGround:
    pass


class ShipHitEnemy:
    pass


class RocketHitGround:
    def __init__(self, coords, blast_radius):
        self.coords = coords
        self.blast_radius = blast_radius


class RocketHitMovable:
    pass

class RocketHitGround:
    def __init__(self, coords, blast_radius):
        self.coords = coords
        self.blast_radius = blast_radius


class EnemyShoot:
    def __init__(self, rocket):
        self.rocket = rocket


class ShipDead:
    pass

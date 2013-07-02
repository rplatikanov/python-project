class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vec2D):
            return NotImplemented
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vec2D):
            return NotImplemented
        return Vec2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __mul__(self, other):
        return Vec2D(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vec2D(self.x * other, self.y * other)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y

        raise IndexError()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

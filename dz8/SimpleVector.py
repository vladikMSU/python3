class Vector:
    def __init__(self, a, b, c):
        self.x, self.y, self.z = float(a), float(b), float(c)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, coeff):
        return Vector(self.x * coeff, self.y * coeff, self.z * coeff)

    def __rmul__(self, coeff):
        return Vector(self.x * coeff, self.y * coeff, self.z * coeff)

    def __truediv__(self, coeff):
        return Vector(self.x / coeff, self.y / coeff, self.z / coeff)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return "{:.2f}:{:.2f}:{:.2f}".format(self.x, self.y, self.z)
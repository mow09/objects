"""1D, 2D and 3D Positions in coordinate systems."""


from math import sqrt


class Point1D:
    """Is a point in a coordinate system."""

    def __init__(self, x):
        """Initiale coordinate points."""
        self.x = x
        self.position = self.x

    @property
    def data(self):
        """Return data."""
        return self.x

    def get_distance(self, other):
        """Calculate the euclidean distance."""
        # print(type(self.data), type(other.data))
        # assert type(self.data) == type(other)
        return sqrt((self.data - other.data)**2)

    def get_center(self, other):
        """Get Center Point."""
        # print(type(self.x), self.x, other.x, type(other.x))
        return Point1D((self.x+other.x)/2)

    def __add__(self, other):
        """Return addition for add operation."""
        return Point1D((self.x + other))

    def __truediv__(self, other):
        """Return devision for div operation."""
        return Point1D((self.x / other))

    def __lt__(self, other):
        """Return the less than function for sorted(x0,...,xn)."""
        return self.x < other.x

    def __repr__(self):
        """Return the information."""
        return f"{self.x}"

    def __str__(self):
        """Return the str information."""
        return f"(x) = ({self.x})"


class Point2D(Point1D):
    """Is a 2D position in a coordinate system."""

    def __init__(self, x, y):
        """Initiale coordinate points."""
        Point1D.__init__(self, x)
        self.y = Point1D(y).data
        self.position = self.x, self.y

    @property
    def data(self):
        """Return data."""
        return self.x, self.y

    def get_distance(self, other):
        """Calculate the euclidean distance."""
        assert type(self) == type(other)
        return sqrt((self.x - other.x)**2+(self.y - other.y)**2)

    def get_center(self, other):
        """Get Center Point."""
        # print(type(self.x), self.x, other.x, type(other.x))
        return Point2D((self.x+other.x)/2, (self.y+other.y)/2)

    def __repr__(self):
        """Return the information."""
        return f"{self.x}, {self.y}"

    def __str__(self):
        """Return the information."""
        return f"(x, y) = ({self.x}, {self.y})"


class Point3D(Point2D):
    """Is a position in a coordinate system."""

    def __init__(self, x, y, z):
        """Initiale coordinate points."""
        # super(Point3D, self).__init__(self, x, y)
        Point2D.__init__(self, x, y)
        self.z = Point1D(z).data
        self.position = self.x, self.y, self.z

    @property
    def data(self):
        """Return data."""
        return self.x, self.y, self.z

    def get_distance(self, other):
        """Calculate the euclidean distance."""
        assert type(self) == type(other)
        return sqrt((self.x - other.x)**2
                    + (self.y - other.y)**2
                    + (self.z - other.z)**2)

    def get_center(self, other):
        """Get Center Point."""
        # print(type(self.x), self.x, other.x, type(other.x))
        return Point3D((self.x+other.x)/2,
                       (self.y+other.y)/2,
                       (self.z+other.z)/2)

    def __repr__(self):
        """Return the information."""
        return f"{self.x}, {self.y}, {self.z}"

    def __str__(self):
        """Return the str information."""
        return f"(x, y, z) = ({self.x}, {self.y}, {self.z})"


def main():
    """Call it if its run as main."""
    p11 = Point1D(1)
    p12 = Point1D(2)
    assert p12.position == (2) == p12.data

    p21 = Point2D(1, 1)
    p22 = Point2D(2, 2)
    assert p22.position == (2, 2) == p22.data

    p31 = Point3D(1, 1, 1)
    p32 = Point3D(2, 2, 2)
    assert p32.position == (2, 2, 2) == p32.data

    dist1 = p11.get_distance(p12)
    assert round(dist1, 6) == 1.0
    dist2 = p21.get_distance(p22)
    assert round(dist2, 6) == 1.414214
    dist3 = p31.get_distance(p32)
    assert round(dist3, 6) == 1.732051

    cent1 = p11.get_center(p12)
    assert cent1.data == 1.5
    cent2 = p21.get_center(p22)
    assert cent2.data == (1.5, 1.5)
    cent3 = p31.get_center(p32)
    assert cent3.data == (1.5, 1.5, 1.5)


if __name__ == '__main__':
    main()

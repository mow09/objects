"""A file for mathematic objects in coordinate systems."""

from positions import (Point1D,
                       Point2D,
                       Point3D)
from math import pi, cos, sin
# from positions import (Point1D,
#                        Point2D,
#                        Point3D)
# """For an import from nb it must have a point as followered:
# AND CHECK FOR PYTHONPATH
# """
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/')


class Line1D:
    """A line between two Point1Ds."""

    def __init__(self, p1, p2):
        """Initiale points for a 2D line."""
        self.p1 = p1  # Point1D
        self.p2 = p2  # Point1D

    @property
    def data(self):
        """Return data."""
        return self.p1, self.p2

    def get_line_points(self, approx):
        """Get points on the line between line-points."""
        # self.point_list = list()
        # self.center = self.get_center(self.p1, self.p2)
        point_list = []
        pre = self.p1.get_center(self.p2)
        # print('pre', type(pre))
        point_list.append(pre)

        x0 = min(self.p1, self.p2)
        # print('x0: ', type(x0.data))
        for k in range(1, approx):
            pre = x0.get_center(pre)
            dist = x0.get_distance(pre)
            point_list.append(pre)
            for i in range(1, 2**k):
                point_list.append(pre+dist*(2*i))
        # print(self.point_list)
        # return sorted(self.point_list)
        # print(point_list)
        return sorted(point_list)

    def __repr__(self):
        """Return the information."""
        return f"{self.p1}, {self.p2}"

    def __str__(self):
        """Return the str information."""
        return f"(p1, p2) = ({self.p1}, {self.p2})"


class Line2D:
    """A line between two Point2D."""

    def __init__(self, p1, p2):
        """Initiale points for a 2D line."""
        self.p1 = Point2D(p1[0], p1[1])
        self.p2 = Point2D(p2[0], p2[1])

    @property
    def data(self):
        """Return data."""
        return self.p1, self.p2

    def get_line_points(self, approx):
        """Get points on the line between line-points."""
        point_list = []
        pre = self.p1.get_center(self.p2)
        point_list.append(pre)
        xy = min(self.p1, self.p2)
        print('x0: ', type(xy), xy)
        for k in range(1, approx):
            pre = xy.get_center(pre)
            print('pre', type(pre))
            print('pre0', pre.x)
            print('pre1', pre.y)
            distx = Point1D(xy.x).get_distance(Point1D(pre.x))
            disty = Point1D(xy.y).get_distance(Point1D(pre.y))
            print('dist', distx, disty)
            point_list.append(pre)
            for i in range(1, 2**k):
                print('k: ', i)
                point_list.append(Point2D(pre.x+distx*(2*i),
                                          pre.y+disty*(2*i)))
                # print(self.point_list)
                # return sorted(self.point_list)
                # print(point_list)
        return sorted(point_list)

    def __repr__(self):
        """Return the information."""
        return f"{self.p1}, {self.p2}"

    def __str__(self):
        """Return the str information."""
        return f"(p1, p2) = ({self.p1}, {self.p2})"


class Line3D:
    """A line between two Point3D."""

    def __init__(self, p1, p2):
        """Initiale points for a 2D line."""
        self.p1 = Point3D(p1[0], p1[1], p1[2])
        self.p2 = Point3D(p2[0], p2[1], p2[2])

    @property
    def data(self):
        """Return data."""
        return self.p1, self.p2

    def get_line_points(self, approx):
        """Get points on the line between line-points."""
        point_list = []
        pre = self.p1.get_center(self.p2)
        point_list.append(pre)
        xyz = min(self.p1, self.p2)
        print('x0: ', type(xyz), xyz)
        for k in range(1, approx):
            pre = xyz.get_center(pre)
            print('pre', type(pre))
            print('pre0', pre.x)
            print('pre1', pre.y)
            print('pre3', pre.z)
            distx = Point1D(xyz.x).get_distance(Point1D(pre.x))
            disty = Point1D(xyz.y).get_distance(Point1D(pre.y))
            distz = Point1D(xyz.z).get_distance(Point1D(pre.z))
            print('dist', distx, disty, distz)
            point_list.append(pre)
            for i in range(1, 2**k):
                print('k: ', i)
                point_list.append(Point3D(pre.x+distx*(2*i),
                                          pre.y+disty*(2*i),
                                          pre.z+distz*(2*i)))
        return sorted(point_list)

    def __repr__(self):
        """Return the information."""
        return f"{self.p1}, {self.p2}"

    def __str__(self):
        """Return the str information."""
        return f"(p1, p2) = ({self.p1}, {self.p2})"


class Circle(Point2D):
    """Create a Circle and beyond."""

    def __init__(self, x, y, r):
        """Initiale center and radius for circle."""
        Point2D.__init__(self, x, y)
        self.r = Point2D(r, 0).data
        self.center = self.x, self.y
        self.orbit = 2 * pi * r
        self.area = pi * r**2

    def get_rad_list(self, n):
        """Calculate the rad for i=1...n."""
        return [(2*pi*i-2*pi)/n for i in range(1, n+1)]

    def get_orbit_points(self, approx):
        """Calculate n points for the orbit."""
        orbit_points = list()
        """
        Calculating orbit pints with classic linear algebra:
        x' = cos(alpha) * r + x
        y' = sin(alpha) * r + y
        """
        for i in self.get_rad_list(approx):
            orbit_points.append(Point2D(cos(i)*self.r[0]+self.x,
                                        sin(i)*self.r[0]+self.y))
        return orbit_points

    def get_orbit_points_rot(self, approx):
        """Calculate n points for the orbit with rotation matrix."""
        orbit_points = list()
        """Rotation Matrix."""
        for i in self.get_rad_list(approx):
            orbit_points.append(
                Point2D(
                    self.x+(self.r[0]*cos(i)-self.r[1]*sin(i)),
                    self.y+(self.r[0]*sin(i)+self.r[1]*cos(i)))
            )
        return orbit_points

        @property
        def data(self):
            """Return data."""
            return self.x, self.y, self.r

        def __repr__(self):
            """Return the information."""
            return f"{self.x}, {self.y}, {self.r}"

        def __str__(self):
            """Return the str information."""
            return f"(x, y, r) = ({self.x}, {self.y}, {self.r})"


class Sphere(Point3D):
    """Create a Sphere and beyond."""

    def __init__(self, x, y, z, r):
        """Initiale points for circle."""
        Point3D.__init__(self, x, y, z)
        self.r = Point3D(r, 0, 0).data
        self.center = self.x, self.y, self.z
        self.orbit = 2 * pi * r
        self.surface = 4 * pi * r**2
        self.volume = 4/3 * pi * r**3

    def get_rad_list(self, n):
        """Calculate the rad for i=1...n."""
        return [(2*pi*i-2*pi)/n for i in range(1, n+1)]

    def get_orbit_points_on_axis(self, approx, xy_axis=False,
                                 yz_axis=False, zx_axis=False):
        """
        Get the n orbit points of an axis.

        For an orbit on the x,y axis it has to be rotated on z.
        """
        orbit_points = list()
        if xy_axis:  # rotate on z
            self.r = 1, 0, 0
            for i in self.get_rad_list(approx):
                orbit_points.append(
                    Point3D(
                        self.x+(
                            + self.r[0]*cos(i)
                            - self.r[1]*sin(i)
                            + self.r[2]*sin(i)*0),
                        self.y+(
                            + self.r[0]*sin(i)
                            + self.r[1]*cos(i)
                            - self.r[2]*sin(i)*0),
                        self.z+(
                            - self.r[0]*sin(i)*0
                            + self.r[1]*sin(i)*0
                            + self.r[2]*cos(i)*1)
                    ))
        if yz_axis:  # rotate on x
            self.r = 0, 1, 0
            for i in self.get_rad_list(approx):
                orbit_points.append(
                    Point3D(
                        self.x+(
                            + self.r[0]*cos(i)*1
                            - self.r[1]*sin(i)*0
                            + self.r[2]*sin(i)*0),
                        self.y+(
                            + self.r[0]*sin(i)*0
                            + self.r[1]*cos(i)
                            - self.r[2]*sin(i)),
                        self.z+(
                            - self.r[0]*sin(i)*0
                            + self.r[1]*sin(i)
                            + self.r[2]*cos(i))
                    ))
        if zx_axis:  # rotate on y
            self.r = 0, 0, 1
            for i in self.get_rad_list(approx):
                orbit_points.append(
                    Point3D(
                        self.x+(
                            + self.r[0]*cos(i)
                            - self.r[1]*sin(i)*0
                            + self.r[2]*sin(i)),
                        self.y+(
                            + self.r[0]*sin(i)*0
                            + self.r[1]*cos(i)*1
                            - self.r[2]*sin(i)*0),
                        self.z+(
                            - self.r[0]*sin(i)
                            + self.r[1]*sin(i)*0
                            + self.r[2]*cos(i))
                    ))
        return orbit_points

    @property
    def data(self):
        """Return data."""
        return self.x, self.y, self.z, self.r

    def __repr__(self):
        """Return the information."""
        return f"{self.x}, {self.y}, {self.z}, {self.r}"

    def __strr__(self):
        """Return the information."""
        return f"(x, y, z, r) = ({self.x}, {self.y}, {self.z}, {self.r})"


def main():
    """Call the main function."""
    line1D_Point1D_test_list = [Point1D(-10),
                                Point1D(-6.25),
                                Point1D(-2.5),
                                Point1D(1.25),
                                Point1D(5.0),
                                Point1D(8.75),
                                Point1D(12.5),
                                Point1D(16.25),
                                Point1D(20)
                                ]
    p11 = Point1D(-10)
    p12 = Point1D(20)

    l11 = Line1D(p11, p12)

    line_points1 = l11.get_line_points(3)
    line_points1.insert(0, p11)
    line_points1.append(p12)
    for i, j in zip(line1D_Point1D_test_list, line_points1):
        assert i.data == j.data

    p21 = Point2D(-10, -10)
    p22 = Point2D(20, 20)

    l21 = Line2D(p21.data, p22.data)
    l22 = Line2D((-10, -10), (20, 20))
    assert l21.data[0].data == l21.p1.data == l22.data[0].data == l22.p1.data
    assert l21.data[1].data == l21.p2.data == l22.data[1].data == l22.p2.data

    line_points2 = l21.get_line_points(3)
    print('test: ', line_points2)
    line_points2.insert(0, p21)
    line_points2.append(p22)
    for i in line_points2:
        print(type(i), i.data)
    # print(l21.data[0].data, l21.p1.data, l22.data[0].data, l22.p1.data,
    #       l21.data[1].data, l21.p2.data, l22.data[1].data, l22.p2.data)

    p31 = Point3D(-10, -10, -10)
    p32 = Point3D(20, 20, 20)

    l31 = Line3D(p31.data, p32.data)
    l32 = Line3D((-10, -10, -10), (20, 20, 20))
    assert l31.data[0].data == l31.p1.data == l32.data[0].data == l32.p1.data
    assert l31.data[1].data == l31.p2.data == l32.data[1].data == l32.p2.data

    line_points3 = l31.get_line_points(3)
    print('test: ', line_points3)
    line_points3.insert(0, p31)
    line_points3.append(p32)
    for i in line_points3:
        print(type(i), i.data)

    orbit_test_list = [(1.0, 0.0), (0.707107, 0.707107),
                       (0.0, 1.0), (-0.707107, 0.707107),
                       (-1.0, 0.0), (-0.707107, -0.707107),
                       (0.0, -1), (0.707107, -0.707107)]

    for index, (data, data_rot) in enumerate(
            zip(Circle(0, 0, 1).get_orbit_points(8),
                Circle(0, 0, 1).get_orbit_points_rot(8))):
        # print(Point2D(data[0][index], data[1][index]))
        assert (orbit_test_list[index] == (round(data.data[0], 6),
                                           round(data.data[1], 6)))
        # assert (data.data == data_rot.data)

    for index, (data1, data2, data3, data4) in enumerate(zip(
            Sphere(0, 0, 0, 1).get_orbit_points_on_axis(8, xy_axis=True),
            Sphere(0, 0, 0, 1).get_orbit_points_on_axis(8, yz_axis=True),
            Sphere(0, 0, 0, 1).get_orbit_points_on_axis(8, zx_axis=True),
            Circle(0, 0, 1).get_orbit_points(8))):

        assert (round(data1.data[0], 6) ==
                round(data2.data[1], 6) ==
                round(data3.data[2], 6) ==
                round(data4.data[0], 6) ==
                orbit_test_list[index][0])
        assert (round(data1.data[1], 6) ==
                round(data2.data[2], 6) ==
                round(data3.data[0], 6) ==
                round(data4.data[1], 6) ==
                orbit_test_list[index][1])
        assert (round(data1.data[2], 6) ==
                round(data2.data[0], 6) ==
                round(data3.data[1], 6) ==
                0)

    print('\n\n\tThe main just contains tests.\n')


if __name__ == "__main__":
    main()

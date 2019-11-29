"""Test shapes."""

from shapes import Line1D, Line2D, Line3D, Circle, Sphere
from positions import Point1D, Point2D, Point3D

import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_shapes():

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

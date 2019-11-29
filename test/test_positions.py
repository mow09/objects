"""Test positions."""

from positions import Point1D, Point2D, Point3D

import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_positions():
    p11 = Point1D(1)
    p12 = Point1D(2)
    assert p12.position == (2) == p12.data

    # print(p11*5)

    p21 = Point2D(1, 1)
    p22 = Point2D(2, 2)
    assert p22.position == (2, 2) == p22.data

    # print(p22*5)

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

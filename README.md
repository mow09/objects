[![Build Status](https://travis-ci.com/mow09/objects.svg?token=3YzpCr7zqrJRwks2k22w&branch=master)](https://travis-ci.com/mow09/objects)
[![codecov](https://codecov.io/gh/mow09/objects/branch/master/graph/badge.svg?token=ZYABVH5NZ8)](https://codecov.io/gh/mow09/objects)

[![CircleCI](https://circleci.com/gh/mow09/objects/tree/master.svg?style=svg)](https://circleci.com/gh/mow09/objects/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/mow09/objects/badge.svg)](https://coveralls.io/github/mow09/objects)

# Positions
Positions are specific points in k dimensions ![k = {1,2,3}](https://latex.codecogs.com/gif.latex?k%20%3D%20%7B1%2C2%2C3%7D)

### `get_distance()`
![d(\mathbf{p,q})=\sqrt{\sum_{i=1}^n(p_i-q_i)^2}](https://latex.codecogs.com/gif.latex?d%28%5Cmathbf%7Bp%2Cq%7D%29%3D%5Csqrt%7B%5Csum_%7Bi%3D1%7D%5En%28p_i-q_i%29%5E2%7D)

# Shapes
Contains lines in k dimensions ![k = {1,2,3}](https://latex.codecogs.com/gif.latex?k%20%3D%20%7B1%2C2%2C3%7D), circle in 2D and sphere in 3D.

# objects are positions and shapes...

- [x] truediv seems to work in Point1D
- [x] test
- [x] positions
- [x] get_distance
- [x] get_center
- [x] shapes
- [x] ``get_line_points( )``

- over powered using the get_distance from Point1D in Line2D or simple math?!

---

### work in process
Right now it is just a well tested lib with positions and shapes.

---

- [ ] activate pylint
Disables for pylint:
-C0103
-W0612
-R0201
-W0105
-R0914
-W0101

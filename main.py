#!/usr/bin/env python
from Point import Point
from Tetrahedron import Tetrahedron

p = Point(2,2,2)
q = Point(3,-3,-3)
r = Point(-4,-4,-4)
s = Point(5,5,-5)

tetra = Tetrahedron(p,q,r,s)

print tetra.volume()


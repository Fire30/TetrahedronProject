#!/usr/bin/env python

from Point import Point
from Tetrahedron import Tetrahedron
import inspect

print(''\
'Pick four non-coplanar points in R . No point may contain a "0 or 1"'\
'coordinate. All four points must be in different octants.\n')

p = Point(2,2,2)
q = Point(3,-3,-3)
r = Point(-4,-4,-4)
s = Point(5,5,-5)

print('P = %s\nQ = %s\nR = %s\nS = %s\n' % (p,q,r,s))

print ''\
"Part 1- Step One\n"\
    "Find the volume of the tetrahedron created by your four points.\n"
print "tetra = Tetrahedron(p,q,r,s)\n"
    
tetra = Tetrahedron(p,q,r,s)

print inspect.getsource(tetra.volume)

print 'Volume of Tetrahedron = %s\n' % (tetra.volume())

print 'Part 1, Step 2: Find a formula for the volume of any tetrahedron'\
'created by four points, P = (p1,p2, p3) , Q = (q1, q2, q3) ,'\
'R = (r1, r2 , r3), and S = (s1, s2 s3), in terms of the '\
'coordinates of those points.\n'

print 'This is equal to the determinant of the points divide by 6 so...\n'
print '|p1-s1,p2-s2,p3-s3|   1'
print '|q1-s1,q2-s2,q3-s3| * _'
print '|r1-s1,r2-s2,r3-s3|   6\n\n'

print'Part 1: Step 3. Let v1, v 2 , v 3 , v 4 be vectors whose lengths'\
'are equal to the areas of the sides of the tetrahedron opposite the ver'\
'tices P, Q, R, and S respectively, and whose direction is perpendicular '\
'to those sides pointing outward. Show thatv1 + v 2 + v 3 + v 4 = 0 .\n\n'


print inspect.getsource(tetra.prove_areas_add_to_zero)
tetra.prove_areas_add_to_zero()

print'\n\n'\
'Part 2: We are now NOT using your specific tetrahedron. Rather, assume'\
'we have a tetrahedron such that that angles that meet at vertex S are '\
'right angles. Let A, B, and C be the areas of the three faces that meet '\
'at S. Let D be the area of the face oppose S (consisting of the triangle'\
'PQR). Show that A + B + C = D . [NOTE: This is the three dimensional '\
'version of the Pythagorean Theorem] {HINT: Transform the vertex S to the'\
'origin and go from there.}\n\n'

print 'This question is proving, so I do not really have a code solution.'\
      ' You basically make point a = (x,0,0) b = (0,y,0) c = (0,0,z) and d'\
      ' = (0,0,0). Then you get the magnitude of the areas of the vectors '\
      'from those point and then square them. After all the simplication '\
      'you should get (xy)^2 + (yz)^2 + (zx)^2 = (xy)^2 + (yz)^2 + (zx)^2'

print '\n\nYay All Done' 

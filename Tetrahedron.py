from Vector import Vector,PositionVector

class Tetrahedron(object):
    def __init__(self,p,q,r,s):
        self.p = p
        self.q = q
        self.r = r
        self.s = s
    def volume(self):
        
        ps = Vector(self.p,self.s)
        qs = Vector(self.q,self.s)
        rs = Vector(self.r,self.s)
        
        return ps * (qs.cross(rs))/6.0
    def prove_areas_add_to_zero(self):
        v1 = Vector(self.p,self.s).cross(Vector(self.q,self.s)) * .5
        v2 = Vector(self.q,self.s).cross(Vector(self.r,self.s)) * .5
        v3 = Vector(self.r,self.s).cross(Vector(self.p,self.s)) * .5
        v4 = (Vector(self.r,self.s) - Vector(self.p,self.s))\
             .cross(Vector(self.q,self.s) - Vector(self.p,self.s)) * .5
        print
        print 'v1 = %s' % (v1)
        print 'v2 = %s' % (v2)
        print 'v3 = %s' % (v3)
        print 'v4 = %s' % (v4)
        print 'v1 + v2 + v3 + v4 = %s' % (v1 + v2 + v3 + v4)
        

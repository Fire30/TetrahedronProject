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

from Point import Point

class Vector(object):
    def __init__(self,point_a,point_b):
        self.point_a = point_a
        self.point_b = point_b
    def to_position_vector(self):
        x = self.point_b.x - self.point_a.x
        y = self.point_b.y - self.point_a.y
        z = self.point_b.z - self.point_a.z
        return PositionVector(x,y,z)
    def __add__(self,other):
        return self.to_position_vector() + other.to_position_vector()
    def __sub__(self,other):
        return self.to_position_vector() - other.to_position_vector()
    def __mul__(self,other):
        return self.to_position_vector() * other.to_position_vector()
    def cross(self,other):
        return self.to_position_vector().cross(other.to_position_vector())
    def __repr__(self):
        return '%s to %s' % (self.point_a,self.point_b)
    
class PositionVector(Vector):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        Vector.__init__(self,Point(0,0,0),Point(x,y,z))
    def cross(self,other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return PositionVector(x,y,z)
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return PositionVector(x,y,z)
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return PositionVector(x,y,z)
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x + y + z
    def __repr__(self):
        return '<%s,%s,%s>' % (self.x,self.y,self.z)

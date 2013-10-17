class Point(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return '(%s,%s,%s)' % (self.x,self.y,self.z)
    

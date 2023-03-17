import math

class Geometry():
    def __init__(self):
        self.epsg = 3116
        self.type = 'unknown'
        
    def print_details(self):
        print('EPSG: {}, TYPE: {}, VALID: {}'.format(self.epsg, self.type, self.is_valid()))
        
    def is_valid(self):
        return False

class Point(Geometry):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.x = x
        self.y = y
        self.type = 'Point'
        
    def distance_to_point(self, point2):
        if self.is_valid():
            return math.sqrt((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2)
        else:
            return None
            
    def is_valid(self):
        if self.x is None or self.y is None:
            return False
            
        return True
        
class Line(Geometry):
    def __init__(self, point1=None, point2=None):
        super().__init__()
        self.points = [point1, point2]
        self.type = 'Line'
        
    def length(self):
        if self.is_valid():
            return self.points[0].distance_to_point(self.points[1])
        else:
            return None
            
    def is_valid(self):
        if self.points[0].is_valid() and self.points[1].is_valid():
            return True
            
        return False
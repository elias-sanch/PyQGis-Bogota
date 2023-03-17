import math

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
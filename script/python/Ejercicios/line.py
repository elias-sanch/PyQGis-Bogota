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
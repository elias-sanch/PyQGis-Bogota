class Geometry():
    def __init__(self):
        self.epsg = 3116
        self.type = 'unknown'
        
    def print_details(self):
        print('EPSG: {}, TYPE: {}, VALID: {}'.format(self.epsg, self.type, self.is_valid()))
        
    def is_valid(self):
        return False
import math

class Punto:

    # Costruttore
    def __init__(self, x = 0, y = 0):
        
        self.x = x
        
        self.y = y

    # SET && GET
    def setX(self, x):
        
        self.x = x
        
    def setY(self, y):
        
        self.y = y
        
    def getX(self):
        
        return self.x
        
    def getY(self):
        
        return self.y
        
    # Metodi
    def distanza(self, p):
        
        return (math.fabs(self.x - p.x), math.fabs(self.y - p.y))

    def punto_medio(self, p):
        
        return (self.x + math.fabs(self.x - p.x) / 2, self.y + math.fabs(self.y - p.y) / 2)
    
    def __str__(self):
        
        return "x: {}, y: {}".format(self.x, self.y)
    
if __name__ == '__main__':
    
    p = Punto()

    print(p.distanza(Punto()))
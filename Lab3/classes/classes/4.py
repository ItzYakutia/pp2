import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return f"({self.x}, {self.y})"
    def move(self, xnew, ynew):
        self.xnew = xnew + self.x
        self.ynew = ynew + self.y
        return f"({self.xnew}, {self.ynew})"
    def dist(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        return (math.sqrt((self.x1 - self.x)**2 + (self.y1 - self.y)**2))

        
point = Point(5, 4)
print(point.show())
print(point.move(3, 2))
print(point.dist(6, 7))


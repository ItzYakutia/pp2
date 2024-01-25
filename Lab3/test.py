class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__() 
        self.length = length

    def area(self):
        return self.length ** 2

# Create instances of Shape and Square
shape = Shape()
print("Area of Shape:", shape.area())

square = Square(4)
print("Area of Square:", square.area())


Define a class named Rectangle which inherits from 
Shape class from task 2. Class instance can be constructed by a length 
and width. The Rectangle class has a method which can compute the area.
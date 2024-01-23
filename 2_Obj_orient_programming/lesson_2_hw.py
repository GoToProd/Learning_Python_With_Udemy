class Shape:
    def __init__(self):
        print("Shape created")
        
    def draw(self):
        print("Drawing a Shape")
        
    def area(self):
        print("Calculated area")
        
    def perimetr(self):
        print("Calculated perimetr")
        
shape = Shape()

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        print("Rectangle created")
        
        
    def draw(self):
        print(f'Drawing rectangle with width = {self.width} and height = {self.height}')
        
    def area(self):
        return (print(f'Area: {self.width * self.height}'))

    def perimetr(self):
        return (print(f'Perimetr: {(self.width + self.height) * 2}'))
    
rectangle = Rectangle(2,4)
rectangle.draw()
rectangle.perimetr()
rectangle.area()

import math
class Triangle(Shape):
    def __init__(self,a,b,c):
        Shape.__init__(self)
        self.a = a
        self.b = b 
        self.c = c 
        print("Triangle created")
        
    def draw(self):
        print(f'Drawing triangle with "a" = {self.a}, "b" = {self.b}, "c" = {self.c}')
        
    def area (self):
        s = (self.a + self.b + self.c) / 2
        return print(f'Area: {math.sqrt(s * (s-self.a) * (s-self.b) * (s - self.c))}')
    
    def perimetr(self):
        return print(f'Perimetr: {(self.a + self.b + self.c)}')
        
        
triangle = Triangle(13,21,23)
triangle.draw()
triangle.area()
triangle.perimetr()

print(f'Rectangle and Triangle started for shape')
for shape in [rectangle,triangle]:
    shape.draw()
print(f'Rectangle and Triangle stoped for shape')
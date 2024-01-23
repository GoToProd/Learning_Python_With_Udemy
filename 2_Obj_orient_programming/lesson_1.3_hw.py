class Rectangle():
    def __init__ (self):
        self._width = 0
        self._height = 0

        
    def get_width (self):
        return self._width
    
    def get_height (self):
        return self._height
    
    def set_width (self, width):
        self._width = width
        
    def set_height (self, height):
        self._height = height
        
    def area (self):
        return self._width * self._height
    
rectangle = Rectangle()

width = float(input("Введите ширину прямоугольника: "))
rectangle.set_width(width)
height = float(input("Введите высоту прямоугольника: "))
rectangle.set_height(height)

print("Ширина прямоугольника:", rectangle.get_width())
print("Высота прямоугольника:", rectangle.get_height())

# Вычисляем и выводим площадь прямоугольника
print("Площадь прямоугольника:", rectangle.area())


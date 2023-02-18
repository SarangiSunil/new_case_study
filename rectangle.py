os.getcwd()
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Parallelepiped(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height
import Rectangle 

rect = rectangle.Rectangle(5, 10)
print("Rectangle area:", rect.area())
print("Rectangle perimeter:", rect.perimeter())

para = rectangle.Parallelepiped(5, 10, 15)
print("Parallelepiped volume:", para.volume())


# pour faire abstract methodes il faut import le module
from abc import ABC ,abstractclassmethod
class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass

class  Square(Shape):
    def __init__(self,side):
        self.__side=side

    def area(self):
        return self.__side*self.__side

    def perimeter(self):
        return self.__side*4


class Rect(Shape):
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def area(self):
        return self.__length*self.__width

    def perimeter(self):
        return (self.__width+self.__length)*2

square = Square(10)
print(f"la surface est {square.area()} et le perimetre est {square.perimeter()}")
Rectangle = Rect(5,2)
print(f"la surface est {Rectangle.area()} et le perimetre est {Rectangle.perimeter()}")
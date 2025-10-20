#EX 1
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length=5, breadth=3):
        self.length = length
        self.breadth = breadth
    
    def calculate_area(self):
        area = self.length * self.breadth
        print("Rectangle Area:", area)

class Circle(Shape):
    def __init__(self, radius=4):
        self.radius = radius
    
    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        print("Circle Area:", area)

rect = Rectangle()
rect.calculate_area()

circ = Circle()
circ.calculate_area()


#EX 2
class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        print("Length:", self.__length)
        print("Breadth:", self.__breadth)

rect = Rectangle(10, 5)


#EX 3
class Fish:
    def type(self):
        print("fish")

class Shark(Fish):
    def type(self):
        print("shark")

obj_goldfish = Fish()
obj_hammerhead = Shark()

for obj in [obj_goldfish, obj_hammerhead]:
    obj.type()


#EX 4
class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, o):
        if self.a < o.a:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"

ob1 = A(5)
ob2 = A(10)

print(ob1 < ob2)


#EX 5
class Beans:
    def type(self):
        print("Vegetable")
    def color(self):
        print("Green")

class Mango:
    def type(self):
        print("Fruit")
    def color(self):
        print("Yellow")

def func(obj):
    obj.type()
    obj.color()

beans = Beans()
mango = Mango()

func(beans)
func(mango)

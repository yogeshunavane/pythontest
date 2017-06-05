'''

# Factory/shapefact1/ShapeFactory1.py
# A simple static factory method.
from __future__ import generators
import random

class Shape(object):
    # Create based on class name:
    def factory(type):
        #return eval(type + "()")
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

# Generate shape name strings:
def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = \
  [ Shape.factory(i) for i in shapeNameGen(3)]

for shape in shapes:
    shape.draw()
    shape.erase()
'''

class Car(object):
 
    def factory(type):
        if type == "Racecar": 
            return Racecar()
        if type == "Van": 
            return Van()
        assert 0, "Bad car creation: " + type
 
    factory = staticmethod(factory)
 
class Racecar(Car):
    def drive(self): print("Racecar driving.")
 
class Van(Car):
    def drive(self): print("Van driving.")
 
# Create object using factory.
obj = Car.factory("Racecar")
obj.drive()
obj2 = Car.factory("Racecar")
print(obj)
print(obj2)

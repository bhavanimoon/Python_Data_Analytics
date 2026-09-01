# Intro to Class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Draw")


point1 = Point(10, 15)
print(point1.x)
print(point1.y)
point1.draw()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Talk method invoked")
        print(f"Hi I am {self.name}. Pangavayo!")

per = Person("Bhavani")
print(per.name)
per.talk()

ap = Person("Appunu")
ap.talk()


'''
# simple class without constructor (__init__)

class Point:
    def draw(self):
        print("Draw")

    def mark(self):
        print("Mark")


p1 = Point()
p1.x = 10
p1.y = 20
p1.draw()
print(p1.x)

p2 = Point()
p2.y = 30
p2.mark()
print(p2.y)
'''


# Inheritance

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("I'm a dog and I bark!!")


class Cat(Mammal):
    def meow(self):
        print("I'm a cat and I meow..")

ani = Dog()
ani.bark()
ani.walk()

me = Cat()
me.meow()
me.walk()
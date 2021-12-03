# class Point:
#     def __init__(self,x ,y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print('move')
#
#     def draw(self):
#         print('draw')
#
#
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def talk(self):
#         print('talk')
#
# ifte = Person('ifte')
# print(ifte.name)
# ifte.talk()

class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def berk(self):
        print('berk')

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.berk()
cat1 = Cat()
cat1.walk()
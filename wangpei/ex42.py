#!/usr/bin/env python
# coding=utf-8
class Animal(object):
    pass
class Dog(Animal):
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def __init__(self,name):
        self.name = name

class Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)#py3中super语法的改变,要使用super函数必须要让父类继承自object类，这是python的新式类支持的特性
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass
class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank",120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

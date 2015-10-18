#!/usr/bin/env python
# coding=utf-8

class Parent(object):

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    #pass
    def implicit(self):
        print("Hello")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

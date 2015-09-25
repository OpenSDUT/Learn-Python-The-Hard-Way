#!/usr/bin/env python
# coding=utf-8
name = 'Zed A . Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = "Brown"

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#毛？
print "If I add %d,%d,and %d I get %d." %  (
    age,height,weight,age + height + weight
)

#啥都吐？
print "%r %r %r %r %r %r" % (1,'2',(3,4),[5,6],{7:8},"Hello World!")

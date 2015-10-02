#!/usr/bin/env python
# coding=utf-8
ten_things="Apples Oranges Crows Telephone Light Suger"
print "Wait there's not 10 thing in that list ,let's fix that"
stuff=ten_things.split(" ")
more_stuff=['Day','Night','Song','Frisbee','Corn','Banana','Girl','Boy']
while len(stuff)!=10:
    next_one=more_stuff.pop()
    print "Adding:",next_one
    stuff.append(next_one)
    print "There 's %d items now."%len(stuff)
print "There we go :",stuff
print "Let's do some thing with stuff."
print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff)
print "#".join(stuff)
